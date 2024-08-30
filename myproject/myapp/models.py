# myapp/models.py
from django.db import models

class Order(models.Model):
    order_code = models.CharField(max_length=100)
    order_name = models.CharField(max_length=255)
    order_loinc_code = models.CharField(max_length=100)
    loinc_name = models.CharField(max_length=255)
    order_loinc_description = models.TextField()

    def __str__(self):
        return self.order_code
    
class SpecimenType(models.Model):
    order = models.ForeignKey(Order, related_name='specimen_types', on_delete=models.CASCADE)
    specimen_type = models.CharField(max_length=255)

    def __str__(self):
        return self.specimen_type

class SpecimenTypeSNOMEDCode(models.Model):
    specimen_type = models.ForeignKey(SpecimenType, related_name='snomed_codes', on_delete=models.CASCADE)
    specimen_type_snomed_code = models.CharField(max_length=100)

    def __str__(self):
        return self.specimen_type_snomed_code

class SourceDescription(models.Model):
    specimen_type_snomed_code = models.ForeignKey(SpecimenTypeSNOMEDCode, related_name='source_descriptions', on_delete=models.CASCADE)
    source_description = models.TextField()

    def __str__(self):
        return self.source_description

class SpecimenSource(models.Model):
    source_description = models.ForeignKey(SourceDescription, related_name='specimen_sources', on_delete=models.CASCADE)
    specimen_source = models.CharField(max_length=255)

    def __str__(self):
        return self.specimen_source

class SourceSNOMEDCode(models.Model):
    specimen_source = models.ForeignKey(SpecimenSource, related_name='snomed_codes', on_delete=models.CASCADE)
    source_snomed_code = models.CharField(max_length=100)

    def __str__(self):
        return self.source_snomed_code

class Specimen(models.Model):
    order = models.ForeignKey(Order, related_name='specimens', on_delete=models.CASCADE)
    specimen_type = models.ForeignKey(SpecimenType, related_name='specimens', on_delete=models.CASCADE)
    specimen_type_snomed_code = models.ForeignKey(SpecimenTypeSNOMEDCode, related_name='specimens', on_delete=models.CASCADE)
    source_description = models.ForeignKey(SourceDescription, related_name='specimens', on_delete=models.CASCADE)
    specimen_source = models.ForeignKey(SpecimenSource, related_name='specimens', on_delete=models.CASCADE)
    source_snomed_code = models.ForeignKey(SourceSNOMEDCode, related_name='specimens', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.specimen_type} - {self.specimen_source}"
    

class District(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Define the TestLocation model
class TestLocation(models.Model):
    location_name = models.CharField(max_length=255)
    district = models.ForeignKey(District, related_name='test_locations', on_delete=models.CASCADE)

    def __str__(self):
        return self.location_name

# Define the OrderingPhysicianNPI model
class OrderingPhysicianNPI(models.Model):
    npi_code = models.CharField(max_length=100)
    test_location = models.ForeignKey(TestLocation, related_name='ordering_physicians', on_delete=models.CASCADE)

    def __str__(self):
        return self.npi_code

# Define the Submitter model
class Submitter(models.Model):
    submitter_code = models.CharField(max_length=100, unique=True)  # Ensure submitter_code is unique
    district = models.ForeignKey(District, related_name='submitters', on_delete=models.CASCADE)
    test_location = models.ForeignKey(TestLocation, related_name='submitters', on_delete=models.CASCADE)
    ordering_physician_npi = models.ForeignKey(OrderingPhysicianNPI, related_name='submitters', on_delete=models.CASCADE)
    collection_date = models.DateField()
    collection_time = models.TimeField()

    def __str__(self):
        return self.submitter_code
    
class Gender(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Ethnicity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Environment(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Patient(models.Model):
    patient_first_name = models.CharField(max_length=255)
    patient_middle_name = models.CharField(max_length=255, blank=True, null=True)
    patient_last_name = models.CharField(max_length=255)
    patient_gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    dob = models.DateField()
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    zip = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, null=True)
    ethnicity = models.ForeignKey(Ethnicity, on_delete=models.SET_NULL, null=True)
    entry_number = models.CharField(max_length=100)
    env = models.ForeignKey(Environment, on_delete=models.SET_NULL, null=True)
    extract_flag = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient_first_name} {self.patient_last_name}"