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

class Specimen(models.Model):
    order = models.ForeignKey(Order, related_name='specimens', on_delete=models.CASCADE)
    specimen_id = models.CharField(max_length=100)
    specimen_type = models.CharField(max_length=255)
    specimen_type_snomed_code = models.CharField(max_length=100)
    source_description = models.TextField()
    specimen_source = models.CharField(max_length=255)
    source_snomed_code = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.specimen_type} - {self.specimen_source}"

class Submitter(models.Model):
    submitter_code = models.CharField(max_length=100)
    district = models.CharField(max_length=255)
    orderingphysiciannpi = models.CharField(max_length=100)
    collectiondate = models.DateField()
    collectiontime = models.TimeField()
    testlocation = models.CharField(max_length=255)

    def __str__(self):
        return self.submitter_code

class Patient(models.Model):
    patient_first_name = models.CharField(max_length=255)
    patient_middle_name = models.CharField(max_length=255, blank=True, null=True)
    patient_last_name = models.CharField(max_length=255)
    patient_gender = models.CharField(max_length=10)
    dob = models.DateField()
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    race = models.CharField(max_length=50)
    ethnicity = models.CharField(max_length=50)
    entry_number = models.CharField(max_length=100)
    env = models.CharField(max_length=50)
    extract_flag = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient_first_name} {self.patient_last_name}"
