import React from 'react';
import { FormControl, InputLabel, MenuItem, Select, SelectChangeEvent, TextField } from '@mui/material';

type FormInputProps = {
  label: string;
  value: string;
  onChange: (event: React.ChangeEvent<HTMLInputElement> | SelectChangeEvent<string>) => void;
  options?: string[]; // If options are provided, render a Select, otherwise render a TextField
  isDropdown?: boolean; // Optional flag to explicitly mark this as a dropdown
  readOnly?: boolean;
};

const FormInput: React.FC<FormInputProps> = ({ label, value, onChange, options, isDropdown, readOnly = false }) => {
  return (
    <FormControl fullWidth margin="normal">
      <InputLabel>{label}</InputLabel>
      {options || isDropdown ? (
        <Select value={value} onChange={onChange} label={label}>
          {options?.map((option) => (
            <MenuItem key={option} value={option}>
              {option}
            </MenuItem>
          ))}
        </Select>
      ) : (
        <TextField
          value={value}
          onChange={onChange as React.ChangeEventHandler<HTMLInputElement>}
          label={label}
          InputProps={{ readOnly }}
        />
      )}
    </FormControl>
  );
};

export default FormInput;
