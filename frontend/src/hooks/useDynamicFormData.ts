import { useState, useEffect } from 'react';
import api, { fetchOrders } from '../utils/axios';
import { Order } from '../types/api';
import { API_PATH } from '../utils/appRoutes';
import { SelectChangeEvent } from '@mui/material';

// Define types for dropdown data as strings
type DropdownData = {
  specimenTypes: string[];
  specimenTypeSnomedCodes: string[];
  sourceDescriptions: string[];
  specimenSources: string[];
  sourceSnomedCodes: string[];
  districts: string[];
  physicianNpis: string[];
  collectionDates: string[];
  collectionTimes: string[];
  testLocations: string[];
  races: string[];
  ethnicities: string[];
  entryNumbers: string[];
  envs: string[];
  extractFlags: string[];
};

// Initial dropdown data structure
const initialDropdownData: DropdownData = {
  specimenTypes: [],
  specimenTypeSnomedCodes: [],
  sourceDescriptions: [],
  specimenSources: [],
  sourceSnomedCodes: [],
  districts: [],
  physicianNpis: [],
  collectionDates: [],
  collectionTimes: [],
  testLocations: [],
  races: [],
  ethnicities: [],
  entryNumbers: [],
  envs: [],
  extractFlags: []
};

// Full data structures to maintain state for objects
type FullData = {
  specimenTypes: any[];
  specimenTypeSnomedCodes: any[];
  sourceDescriptions: any[];
  specimenSources: any[];
  sourceSnomedCodes: any[];
};

// Initial full data structure
const initialFullData: FullData = {
  specimenTypes: [],
  specimenTypeSnomedCodes: [],
  sourceDescriptions: [],
  specimenSources: [],
  sourceSnomedCodes: []
};

export const useDynamicFormData = () => {
  const [orders, setOrders] = useState<Order[]>([]);
  const [selectedOrder, setSelectedOrder] = useState<string>('');
  const [drawerOpen, setDrawerOpen] = useState<boolean>(true);
  const [dropdownData, setDropdownData] = useState<DropdownData>(initialDropdownData);
  const [fullData, setFullData] = useState<FullData>(initialFullData);

  const [textFields, setTextFields] = useState({
    patientFirstName: '',
    patientMiddleName: '',
    patientLastName: '',
    dob: '',
    addressLine1: '',
    addressLine2: '',
    zip: '',
    email: '',
    phoneNumber: '',
    specimenType: '',
    specimenTypeSnomedCode: '',
    sourceDescription: '',
    specimenSource: '',
    sourceSnomedCode: ''
  });

  const selectedOrderValue = orders.find(o => o.order_code === selectedOrder);

  useEffect(() => {
    const loadSpecimenRelatedData = async () => {
      try {
        const [specimenTypeSnomedCodes, sourceDescriptions, specimenSources, sourceSnomedCodes] = await Promise.all([
          api.get(`${API_PATH.SPECIMEN_TYPE_SNOMED_CODES}?specimen_type=${textFields.specimenType}`).then(res => res.data),
          api.get(`${API_PATH.SOURCE_DESCRIPTIONS}?specimen_type_snomed_code=${textFields.specimenTypeSnomedCode}`).then(res => res.data),
          api.get(`${API_PATH.SPECIMEN_SOURCES}?source_description=${textFields.sourceDescription}`).then(res => res.data),
          api.get(`${API_PATH.SOURCE_SNOMED_CODES}?specimen_source=${textFields.specimenSource}`).then(res => res.data)
        ]);

        setFullData(prevData => ({
          ...prevData,
          specimenTypeSnomedCodes,
          sourceDescriptions,
          specimenSources,
          sourceSnomedCodes
        }));

        setDropdownData(prevData => ({
          ...prevData,
          specimenTypeSnomedCodes: specimenTypeSnomedCodes.map(s => s.specimen_type_snomed_code), // Extracting only the relevant string
          sourceDescriptions: sourceDescriptions.map(s => s.source_description),
          specimenSources: specimenSources.map(s => s.specimen_source),
          sourceSnomedCodes: sourceSnomedCodes.map(s => s.source_snomed_code)
        }));
      } catch (error) {
        console.error("Error loading specimen-related data:", error);
      }
    };

    if (textFields.specimenType) {
      const specimentType = textFields.specimenType;
      const specimentTypeId = fullData.specimenTypes.find(s => s.specimen_type === specimentType)?.id;
      console.log('updated textFields', specimentType, textFields, specimentTypeId)
      loadSpecimenRelatedData();
    }
  }, [textFields.specimenType, textFields.specimenTypeSnomedCode, textFields.sourceDescription, textFields.specimenSource]);

  useEffect(() => {
    const loadOrders = async () => {
      try {
        const fetchedOrders = await fetchOrders();
        setOrders(fetchedOrders);
      } catch (error) {
        console.error("Error fetching orders:", error);
      }
    };

    const loadDropdownData = async () => {
      try {
        const specimenTypes = await api.get(API_PATH.SPECIMEN_TYPES).then(res => res.data);

        setFullData(prevData => ({
          ...prevData,
          specimenTypes
        }));

        setDropdownData(prevData => ({
          ...prevData,
          specimenTypes: specimenTypes.map(s => s.specimen_type) // Extracting only the relevant string
        }));
      } catch (error) {
        console.error("Error loading dropdown data:", error);
      }
    };

    loadOrders();
    loadDropdownData();
  }, []);

  const handleDrawerToggle = () => {
    setDrawerOpen(!drawerOpen);
  };

  const handleOrderChange = (event: SelectChangeEvent<string>) => {
    setSelectedOrder(event.target.value as string);
  };

  const handleTextChange = (field: string) => (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement> | SelectChangeEvent<string>) => {
    console.log("handleTextChange", field, event.target.value)
    setTextFields(prevFields => ({
      ...prevFields,
      [field]: event.target.value
    }));
  };

  const resetForm = () => {
    setSelectedOrder('');
    setTextFields({
      patientFirstName: '',
      patientMiddleName: '',
      patientLastName: '',
      dob: '',
      addressLine1: '',
      addressLine2: '',
      zip: '',
      email: '',
      phoneNumber: '',
      specimenType: '',
      specimenTypeSnomedCode: '',
      sourceDescription: '',
      specimenSource: '',
      sourceSnomedCode: ''
    });
  };

  return {
    orders,
    selectedOrder,
    selectedOrderValue,
    drawerOpen,
    dropdownData,
    fullData,
    textFields,
    handleDrawerToggle,
    handleOrderChange,
    handleTextChange,
    resetForm
  };
};
