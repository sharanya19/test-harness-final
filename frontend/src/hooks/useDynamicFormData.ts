// hooks/useDynamicFormData.ts
import { useState, useEffect } from 'react';
import { fetchOrders, fetchDropdownData } from '../utils/axios';
import { Order } from '../types/api';
import { SelectChangeEvent } from '@mui/material';

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

export const useDynamicFormData = () => {
  const [orders, setOrders] = useState<Order[]>([]);
  const [selectedOrder, setSelectedOrder] = useState<string>('');
  const [drawerOpen, setDrawerOpen] = useState<boolean>(true);
  const [dropdownData, setDropdownData] = useState<DropdownData>(initialDropdownData);
  const [textFields, setTextFields] = useState({
    patientFirstName: '',
    patientMiddleName: '',
    patientLastName: '',
    dob: '',
    addressLine1: '',
    addressLine2: '',
    zip: '',
    email: '',
    phoneNumber: ''
  });

  const selectedOrderSpecimen = orders.find(o => o.order_code === selectedOrder)?.specimens || []

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
        const dropdownKeys = [
          'SPECIMEN_TYPE',
          'SPECIMEN_TYPE_SNOMED_CODE',
          'SOURCE_DESCRIPTION',
          'SPECIMEN_SOURCE',
          'SOURCE_SNOMED_CODE',
          'DISTRICT',
          'PHYSICIAN_NPI',
          'COLLECTION_DATE',
          'COLLECTION_TIME',
          'TEST_LOCATION',
          'RACE',
          'ETHNICITY',
          'ENTRY_NUMBER',
          'ENV',
          'EXTRACT_FLAG'
        ] as const;

        const dropdownDataPromises = dropdownKeys.map(key => fetchDropdownData(key));
        const resolvedData = await Promise.all(dropdownDataPromises);

        const newDropdownData: DropdownData = {
          specimenTypes: resolvedData[0],
          specimenTypeSnomedCodes: resolvedData[1],
          sourceDescriptions: resolvedData[2],
          specimenSources: resolvedData[3],
          sourceSnomedCodes: resolvedData[4],
          districts: resolvedData[5],
          physicianNpis: resolvedData[6],
          collectionDates: resolvedData[7],
          collectionTimes: resolvedData[8],
          testLocations: resolvedData[9],
          races: resolvedData[10],
          ethnicities: resolvedData[11],
          entryNumbers: resolvedData[12],
          envs: resolvedData[13],
          extractFlags: resolvedData[14]
        };

        setDropdownData(newDropdownData);
      } catch (error) {
        console.error("Error fetching dropdown data:", error);
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

  const handleTextChange = (field: string) => (event: React.ChangeEvent<HTMLInputElement>) => {
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
      phoneNumber: ''
    });
  };

  return {
    orders,
    selectedOrder,
    selectedOrderSpecimen,
    drawerOpen,
    dropdownData,
    textFields,
    handleDrawerToggle,
    handleOrderChange,
    handleTextChange,
    resetForm
  };
};
