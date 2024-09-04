import { useState, useEffect } from 'react';
import api from '../utils/axios';
import { Order, Specimen, SpecimenSource, SpecimenType, SourceDescription, SourceSNOMEDCode, SpecimenTypeSNOMEDCode, City, State, Race, Ethnicity, Environment, Gender, District, TestLocation, OrderingPhysicianNPI, Submitter, CollectionDate, CollectionTime } from '../types/api';
import { API_PATH } from '../utils/appRoutes';
import { SelectChangeEvent } from '@mui/material';

// Define types for dropdown data
type DropdownData = {
  specimenTypes: string[];
  specimenTypeSnomedCodes: string[];
  sourceDescriptions: string[];
  specimenSources: string[];
  sourceSnomedCodes: string[];
  cities: string[];
  states: string[];
  races: string[];
  ethnicities: string[];
  environments: string[];
  genders: string[];
  districts: string[];
  testLocations: string[];
  orderingPhysicians: string[];
  collectionDates: string[];  // New
  collectionTimes: string[];  // New
};

// Initial dropdown data structure
const initialDropdownData: DropdownData = {
  specimenTypes: [],
  specimenTypeSnomedCodes: [],
  sourceDescriptions: [],
  specimenSources: [],
  sourceSnomedCodes: [],
  cities: [],
  states: [],
  races: [],
  ethnicities: [],
  environments: [],
  genders: [],
  districts: [],
  testLocations: [],
  orderingPhysicians: [],
  collectionDates: [],  // New
  collectionTimes: []   // New
};

// Full data structures to maintain state for objects
type FullData = {
  specimenTypes: SpecimenType[];
  specimenTypeSnomedCodes: SpecimenTypeSNOMEDCode[];
  sourceDescriptions: SourceDescription[];
  specimenSources: SpecimenSource[];
  sourceSnomedCodes: SourceSNOMEDCode[];
  cities: City[];
  states: State[];
  races: Race[];
  ethnicities: Ethnicity[];
  environments: Environment[];
  genders: Gender[];
  districts: District[];
  testLocations: TestLocation[];
  orderingPhysicians: OrderingPhysicianNPI[];
  collectionDates: CollectionDate[];  // New
  collectionTimes: CollectionTime[];  // New
};

// Initial full data structure
const initialFullData: FullData = {
  specimenTypes: [],
  specimenTypeSnomedCodes: [],
  sourceDescriptions: [],
  specimenSources: [],
  sourceSnomedCodes: [],
  cities: [],
  states: [],
  races: [],
  ethnicities: [],
  environments: [],
  genders: [],
  districts: [],
  testLocations: [],
  orderingPhysicians: [],
  collectionDates: [],  // New
  collectionTimes: []   // New
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
    sourceSnomedCode: '',
    city: '',
    state: '',
    race: '',
    ethnicity: '',
    environment: '',
    gender: '',
    district: '',
    testLocation: '',
    orderingPhysician: '',
    collectionDate: '',  // New
    collectionTime: ''   // New
  });

  const selectedOrderValue = orders.find(o => o.order_code === selectedOrder);

  useEffect(() => {
    const loadSpecimenRelatedData = async () => {
      try {
        const [specimenTypeSnomedCodes, sourceDescriptions, specimenSources, sourceSnomedCodes] = await Promise.all([
          api.get<SpecimenTypeSNOMEDCode[]>(`${API_PATH.SPECIMEN_TYPE_SNOMED_CODES}?specimen_type=${textFields.specimenType}`).then(res => res.data),
          api.get<SourceDescription[]>(`${API_PATH.SOURCE_DESCRIPTIONS}?specimen_type_snomed_code=${textFields.specimenTypeSnomedCode}`).then(res => res.data),
          api.get<SpecimenSource[]>(`${API_PATH.SPECIMEN_SOURCES}?source_description=${textFields.sourceDescription}`).then(res => res.data),
          api.get<SourceSNOMEDCode[]>(`${API_PATH.SOURCE_SNOMED_CODES}?specimen_source=${textFields.specimenSource}`).then(res => res.data)
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
          specimenTypeSnomedCodes: specimenTypeSnomedCodes.map(s => s.specimen_type_snomed_code),
          sourceDescriptions: sourceDescriptions.map(s => s.source_description),
          specimenSources: specimenSources.map(s => s.specimen_source),
          sourceSnomedCodes: sourceSnomedCodes.map(s => s.source_snomed_code)
        }));
      } catch (error) {
        console.error("Error loading specimen-related data:", error);
      }
    };

    if (textFields.specimenType) {
      loadSpecimenRelatedData();
    }
  }, [textFields.specimenType, textFields.specimenTypeSnomedCode, textFields.sourceDescription, textFields.specimenSource]);

  useEffect(() => {
    const loadOrders = async () => {
      try {
        const fetchedOrders = await api.get<Order[]>(API_PATH.ORDERS).then(res => res.data);
        setOrders(fetchedOrders);
      } catch (error) {
        console.error("Error fetching orders:", error);
      }
    };

    const loadDropdownData = async () => {
      try {
        const [
          specimenTypes,
          cities,
          states,
          races,
          ethnicities,
          environments,
          genders,
          districts,
          testLocations,
          orderingPhysicians,
          collectionDates,
          collectionTimes
        ] = await Promise.all([
          api.get<SpecimenType[]>(API_PATH.SPECIMEN_TYPES).then(res => res.data),
          api.get<City[]>(API_PATH.CITIES).then(res => res.data),
          api.get<State[]>(API_PATH.STATES).then(res => res.data),
          api.get<Race[]>(API_PATH.RACES).then(res => res.data),
          api.get<Ethnicity[]>(API_PATH.ETHNICITIES).then(res => res.data),
          api.get<Environment[]>(API_PATH.ENVIRONMENTS).then(res => res.data),
          api.get<Gender[]>(API_PATH.GENDERS).then(res => res.data),
          api.get<District[]>(API_PATH.DISTRICTS).then(res => res.data),
          api.get<TestLocation[]>(API_PATH.TEST_LOCATIONS).then(res => res.data),
          api.get<OrderingPhysicianNPI[]>(API_PATH.ORDERING_PHYSICIANS).then(res => res.data),
          api.get<CollectionDate[]>(API_PATH.COLLECTION_DATES).then(res => res.data),
          api.get<CollectionTime[]>(API_PATH.COLLECTION_TIMES).then(res => res.data)
        ]);

        setFullData(prevData => ({
          ...prevData,
          specimenTypes,
          cities,
          states,
          races,
          ethnicities,
          environments,
          genders,
          districts,
          testLocations,
          orderingPhysicians,
          collectionDates,
          collectionTimes
        }));

        setDropdownData(prevData => ({
          ...prevData,
          specimenTypes: specimenTypes.map(s => s.specimen_type),
          cities: cities.map(c => c.name),
          states: states.map(s => s.name),
          races: races.map(r => r.name),
          ethnicities: ethnicities.map(e => e.name),
          environments: environments.map(e => e.name),
          genders: genders.map(g => g.name),
          districts: districts.map(d => d.name),
          testLocations: testLocations.map(t => t.location_name),
          orderingPhysicians: orderingPhysicians.map(o => o.npi_code),
          collectionDates: collectionDates.map(c => c.date),
          collectionTimes: collectionTimes.map(t => t.time)
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

  const handleTextChange = (field: string) => (
    event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setTextFields(prevFields => ({
      ...prevFields,
      [field]: event.target.value,
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
      sourceSnomedCode: '',
      city: '',
      state: '',
      race: '',
      ethnicity: '',
      environment: '',
      gender: '',
      district: '',
      testLocation: '',
      orderingPhysician: '',
      collectionDate: '',  // New
      collectionTime: ''   // New
    });
    setDropdownData(initialDropdownData);
    setFullData(initialFullData);
  };

  return {
    orders,
    selectedOrder,
    drawerOpen,
    dropdownData,
    fullData,
    textFields,
    selectedOrderValue,
    handleDrawerToggle,
    handleOrderChange,
    handleTextChange,
    resetForm
  };
};
