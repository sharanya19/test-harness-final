import React from 'react';
import { Button, Drawer, Box } from '@mui/material';
import { useDynamicFormData } from '@/hooks/useDynamicFormData';
import FormInput from '@/components/common/formInput';

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
    resetForm
  } = useDynamicFormData();

  const handleAdd = async () => {
    // Implement functionality to add the record if needed
  };

  return (
    <Drawer
      anchor="right"
      open={drawerOpen}
      onClose={handleDrawerToggle}
      sx={{ width: 600, flexShrink: 0, '& .MuiDrawer-paper': { width: 600, boxSizing: 'border-box' } }}
    >
      <Box sx={{ padding: 2 }}>
        {/* Order Code Dropdown */}
        <FormInput
          label="Order Code"
          value={selectedOrder}
          onChange={handleOrderChange}
          options={orders.map(order => order.order_code)}
          isDropdown
        />

        {/* Display selected order details */}
        {selectedOrder && (
          <Box mt={2}>
            <FormInput
              label="Order Name"
              value={selectedOrderValue?.order_name || ''}
              onChange={() => { }} // Read-only, so no change handler needed
              readOnly
            />
            <FormInput
              label="Order LOINC Code"
              value={selectedOrderValue?.order_loinc_code || ''}
              onChange={() => { }} // Read-only, so no change handler needed
              readOnly
            />
            <FormInput
              label="LOINC Name"
              value={selectedOrderValue?.loinc_name || ''}
              onChange={() => { }} // Read-only, so no change handler needed
              readOnly
            />
            <FormInput
              label="Order LOINC Description"
              value={selectedOrderValue?.order_loinc_description || ''}
              onChange={() => { }} // Read-only, so no change handler needed
              readOnly
            />
          </Box>
        )}

        {/* Additional Dropdowns */}
        {/* Specimen-related Dropdowns */}
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

        {/* Text Fields for typing details */}
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
          value={dropdownData.races[0] || ''}
          onChange={handleTextChange('race')}
          options={dropdownData.races}
        />

        <FormInput
          label="Ethnicity"
          value={dropdownData.ethnicities[0] || ''}
          onChange={handleTextChange('ethnicity')}
          options={dropdownData.ethnicities}
        />

        <FormInput
          label="Entry Number"
          value={dropdownData.entryNumbers[0] || ''}
          onChange={handleTextChange('entryNumber')}
          options={dropdownData.entryNumbers}
        />

        <FormInput
          label="ENV"
          value={dropdownData.envs[0] || ''}
          onChange={handleTextChange('env')}
          options={dropdownData.envs}
        />

        <FormInput
          label="Extract Flag"
          value={dropdownData.extractFlags[0] || ''}
          onChange={handleTextChange('extractFlag')}
          options={dropdownData.extractFlags}
        />

        <Button variant="contained" onClick={handleAdd}>Add</Button>
        <Button variant="outlined" onClick={resetForm}>Discard</Button>
      </Box>
    </Drawer>
  );
};

export default DynamicForm;
