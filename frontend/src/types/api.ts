// types/api.ts

export interface Order {
  id: number;
  order_code: string;
  order_name: string;
  order_loinc_code: string;
  loinc_name: string;
  order_loinc_description: string;
  specimens: Specimen[];
  specimen_types: SpecimenType[];
}

export interface Specimen {
  id: number;
  specimen_type: SpecimenType;
  specimen_type_snomed_code: SpecimenTypeSNOMEDCode;
  source_description: SourceDescription;
  specimen_source: SpecimenSource;
  source_snomed_code: SourceSNOMEDCode;
}

export interface SpecimenType {
  id: number;
  specimen_type: string;
  order: string; // String representation of the order from StringRelatedField
  snomed_codes: SpecimenTypeSNOMEDCode[];
}

export interface SpecimenTypeSNOMEDCode {
  id: number;
  specimen_type: string; // String representation from StringRelatedField
  specimen_type_snomed_code: string;
}

export interface SourceDescription {
  id: number;
  specimen_type_snomed_code: SpecimenTypeSNOMEDCode; // Full object because of nested serializers
  source_description: string;
}

export interface SpecimenSource {
  id: number;
  source_description: SourceDescription; // Full object because of nested serializers
  specimen_source: string;
}

export interface SourceSNOMEDCode {
  id: number;
  specimen_source: SpecimenSource; // Full object because of nested serializers
  source_snomed_code: string;
}

export interface District {
  id: number;
  name: string;
}

export interface TestLocation {
  id: number;
  location_name: string;
  district: District; // Full object reference
}

export interface OrderingPhysicianNPI {
  id: number;
  npi_code: string;
  test_location: TestLocation; // Full object reference
}

export interface CollectionDate {
  id: number;
  date: string; // ISO date string
}

// Interface for CollectionTime
export interface CollectionTime {
  id: number;
  time: string; // Time string in HH:MM:SS format
}

export interface Submitter {
  id: number;
  submitter_code: string;
  district: District; // Full object reference
  test_location: TestLocation; // Full object reference
  ordering_physician_npi: OrderingPhysicianNPI; // Full object reference
  collection_date: CollectionDate; // Full object reference
  collection_time: CollectionTime; 
}

export interface Patient {
  id: number;
  patient_first_name: string;
  patient_middle_name?: string;
  patient_last_name: string;
  patient_gender: Gender;
  dob: string; // ISO date string
  address_line1: string;
  address_line2?: string;
  city: City;
  state: State;
  zip: string;
  email: string;
  phone_number: string;
  race: Race;
  ethnicity: Ethnicity;
  entry_number: string;
  env: Environment;
  extract_flag: boolean;
}

export interface City {
  id: number;
  name: string;
}

export interface State {
  id: number;
  name: string;
  abbreviation: string;
}

export interface Race {
  id: number;
  name: string;
}

export interface Ethnicity {
  id: number;
  name: string;
}

export interface Environment {
  id: number;
  name: string;
}

export interface Gender {
  id: number;
  name: string;
}
