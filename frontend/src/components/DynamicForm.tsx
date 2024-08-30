import React from 'react';
import { Box, Button, Drawer } from '@mui/material';
import FormInput from './common/formInput'; // Ensure FormInput component is correctly imported
import { useDynamicFormData } from '../hooks/useDynamicFormData'; // Ensure useDynamicFormData is correctly imported

const DynamicForm: React.FC = () => {
  const {
    orders,
    selectedOrder,
    selectedOrderValue,
    drawerOpen,
    dropdownData,
    textFields,
    handleDrawerToggle,
    handleOrderChange,
    handleTextChange,
    resetForm,
  } = useDynamicFormData();

  const handleAdd = async () => {
    // Implement functionality to add the record if needed
    console.log('Add functionality needs to be implemented.');
  };

  return (
    <Drawer
      anchor="right"
      open={drawerOpen}
      onClose={handleDrawerToggle}
      sx={{
        width: 600,
        flexShrink: 0,
        '& .MuiDrawer-paper': { width: 600, boxSizing: 'border-box' },
      }}
    >
      <Box sx={{ padding: 2 }}>
        <FormInput
          label="Order Code"
          value={selectedOrder}
          onChange={handleOrderChange}
          options={orders.map((order) => order.order_code)}
          isDropdown
        />

        {selectedOrder && (
          <Box mt={2}>
            <FormInput
              label="Order Name"
              value={selectedOrderValue?.order_name || ''}
              onChange={() => {}} // Read-only
              readOnly
            />
            <FormInput
              label="Order LOINC Code"
              value={selectedOrderValue?.order_loinc_code || ''}
              onChange={() => {}} // Read-only
              readOnly
            />
            <FormInput
              label="LOINC Name"
              value={selectedOrderValue?.loinc_name || ''}
              onChange={() => {}} // Read-only
              readOnly
            />
            <FormInput
              label="Order LOINC Description"
              value={selectedOrderValue?.order_loinc_description || ''}
              onChange={() => {}} // Read-only
              readOnly
            />
            <FormInput
  label="District"
  value={textFields.district}
  onChange={handleTextChange('district')}
  options={dropdownData.districts}
  isDropdown
/>

<FormInput
  label="Test Location"
  value={textFields.testLocation}
  onChange={handleTextChange('testLocation')}
  options={dropdownData.testLocations}
  isDropdown
/>

<FormInput
  label="Ordering Physician"
  value={textFields.orderingPhysician}
  onChange={handleTextChange('orderingPhysician')}
  options={dropdownData.orderingPhysicians}
  isDropdown
/>
          </Box>
        )}

        <FormInput
          label="Specimen Type"
          value={textFields.specimenType}
          onChange={handleTextChange('specimenType')}
          options={dropdownData.specimenTypes}
          isDropdown
        />

        <FormInput
          label="Specimen Type SNOMED Code"
          value={textFields.specimenTypeSnomedCode}
          onChange={handleTextChange('specimenTypeSnomedCode')}
          options={dropdownData.specimenTypeSnomedCodes}
          isDropdown
        />

        <FormInput
          label="Source Description"
          value={textFields.sourceDescription}
          onChange={handleTextChange('sourceDescription')}
          options={dropdownData.sourceDescriptions}
          isDropdown
        />

        <FormInput
          label="Specimen Source"
          value={textFields.specimenSource}
          onChange={handleTextChange('specimenSource')}
          options={dropdownData.specimenSources}
          isDropdown
        />

        <FormInput
          label="Source SNOMED Code"
          value={textFields.sourceSnomedCode}
          onChange={handleTextChange('sourceSnomedCode')}
          options={dropdownData.sourceSnomedCodes}
          isDropdown
        />

        <FormInput
          label="Patient First Name"
          value={textFields.patientFirstName}
          onChange={handleTextChange('patientFirstName')}
        />

        <FormInput
          label="Patient Middle Name"
          value={textFields.patientMiddleName}
          onChange={handleTextChange('patientMiddleName')}
        />

        <FormInput
          label="Patient Last Name"
          value={textFields.patientLastName}
          onChange={handleTextChange('patientLastName')}
        />

        <FormInput
          label="Date of Birth (DOB)"
          value={textFields.dob}
          onChange={handleTextChange('dob')}
        />

        <FormInput
          label="Address Line 1"
          value={textFields.addressLine1}
          onChange={handleTextChange('addressLine1')}
        />

        <FormInput
          label="Address Line 2"
          value={textFields.addressLine2}
          onChange={handleTextChange('addressLine2')}
        />

        <FormInput
          label="ZIP Code"
          value={textFields.zip}
          onChange={handleTextChange('zip')}
        />

        <FormInput
          label="Email"
          value={textFields.email}
          onChange={handleTextChange('email')}
        />

        <FormInput
          label="Phone Number"
          value={textFields.phoneNumber}
          onChange={handleTextChange('phoneNumber')}
        />

        <FormInput
          label="Race"
          value={textFields.race}
          onChange={handleTextChange('race')}
          options={dropdownData.races}
          isDropdown
        />

        <FormInput
          label="Ethnicity"
          value={textFields.ethnicity}
          onChange={handleTextChange('ethnicity')}
          options={dropdownData.ethnicities}
          isDropdown
        />

        <FormInput
          label="Environment"
          value={textFields.environment}
          onChange={handleTextChange('environment')}
          options={dropdownData.environments}
          isDropdown
        />

        <FormInput
          label="Gender"
          value={textFields.gender}
          onChange={handleTextChange('gender')}
          options={dropdownData.genders}
          isDropdown
        />

        <Button variant="contained" onClick={handleAdd}>
          Add
        </Button>
        <Button variant="outlined" onClick={resetForm}>
          Discard
        </Button>
      </Box>
    </Drawer>
  );
};

export default DynamicForm;
