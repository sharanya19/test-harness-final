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

export interface Submitter {
  id: number; 
  submitter_code: string;
  district: string;
  orderingphysiciannpi: string;
  collectiondate: string; // ISO date string
  collectiontime: string; // Time string in HH:MM:SS format
  testlocation: string;
}

export interface Patient {
  id: number; 
  patient_first_name: string;
  patient_middle_name?: string; 
  patient_last_name: string;
  patient_gender: string;
  dob: string; 
  address_line1: string;
  address_line2?: string; 
  city: string;
  state: string;
  zip: string;
  email: string;
  phone_number: string;
  race: string;
  ethnicity: string;
  entry_number: string;
  env: string;
  extract_flag: boolean;
}
