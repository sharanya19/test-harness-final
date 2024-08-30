import React from 'react';
import { FormControl, InputLabel, MenuItem, Select, SelectChangeEvent, TextField } from '@mui/material';

type OnChangeSelect = (event: SelectChangeEvent<string>) => void;

type FormInputProps = {
  label: string;
  value: string;
  onChange: (OnChangeSelect | ((event: React.ChangeEvent<HTMLInputElement>) => void));
  options?: string[];
  isDropdown?: boolean;
  readOnly?: boolean;
};

const FormInput: React.FC<FormInputProps> = ({ label, value, onChange, options, isDropdown, readOnly = false }) => {
  if (isDropdown || options) {
    return (
      <FormControl fullWidth margin="normal">
        <InputLabel>{label}</InputLabel>
        <Select
          value={value}
          onChange={onChange as OnChangeSelect}
          inputProps={{ readOnly }}
        >
          {options?.map((option) => (
            <MenuItem key={option} value={option}>
              {option}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    );
  }
  return (
    <TextField
      fullWidth
      margin="normal"
      label={label}
      value={value}
      onChange={onChange as (event: React.ChangeEvent<HTMLInputElement>) => void}
      InputProps={{ readOnly }}
    />
  );
};

export default FormInput;
