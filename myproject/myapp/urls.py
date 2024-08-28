# myapp/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrderViewSet, 
    SpecimenViewSet, 
    SubmitterViewSet, 
    PatientViewSet, 
    SpecimenTypeDropdownView,
    SpecimenTypeSnomedCodeDropdownView,
    SourceDescriptionDropdownView,
    SpecimenSourceDropdownView,
    SourceSnomedCodeDropdownView,
    DistrictDropdownView,
    PhysicianNpiDropdownView,
    CollectionDateDropdownView,
    CollectionTimeDropdownView,
    TestLocationDropdownView,
    PatientFirstNameDropdownView,
    PatientMiddleNameDropdownView,
    PatientLastNameDropdownView,
    PatientGenderDropdownView,
    DobDropdownView,
    AddressLine1DropdownView,
    AddressLine2DropdownView,
    CityDropdownView,
    StateDropdownView,
    ZipDropdownView,
    EmailDropdownView,
    PhoneNumberDropdownView,
    RaceDropdownView,
    EthnicityDropdownView,
    EntryNumberDropdownView,
    EnvDropdownView,
    ExtractFlagDropdownView
)

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'specimens', SpecimenViewSet)
router.register(r'submissions', SubmitterViewSet)
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dropdown/specimen-type/', SpecimenTypeDropdownView.as_view(), name='specimen_type_dropdown'),
    path('dropdown/specimen-type-snomed-code/', SpecimenTypeSnomedCodeDropdownView.as_view(), name='specimen_type_snomed_code_dropdown'),
    path('dropdown/source-description/', SourceDescriptionDropdownView.as_view(), name='source_description_dropdown'),
    path('dropdown/specimen-source/', SpecimenSourceDropdownView.as_view(), name='specimen_source_dropdown'),
    path('dropdown/source-snomed-code/', SourceSnomedCodeDropdownView.as_view(), name='source_snomed_code_dropdown'),
    path('dropdown/district/', DistrictDropdownView.as_view(), name='district_dropdown'),
    path('dropdown/physician-npi/', PhysicianNpiDropdownView.as_view(), name='physician_npi_dropdown'),
    path('dropdown/collection-date/', CollectionDateDropdownView.as_view(), name='collection_date_dropdown'),
    path('dropdown/collection-time/', CollectionTimeDropdownView.as_view(), name='collection_time_dropdown'),
    path('dropdown/test-location/', TestLocationDropdownView.as_view(), name='test_location_dropdown'),
    path('dropdown/patient-first-name/', PatientFirstNameDropdownView.as_view(), name='patient_first_name_dropdown'),
    path('dropdown/patient-middle-name/', PatientMiddleNameDropdownView.as_view(), name='patient_middle_name_dropdown'),
    path('dropdown/patient-last-name/', PatientLastNameDropdownView.as_view(), name='patient_last_name_dropdown'),
    path('dropdown/patient-gender/', PatientGenderDropdownView.as_view(), name='patient_gender_dropdown'),
    path('dropdown/dob/', DobDropdownView.as_view(), name='dob_dropdown'),
    path('dropdown/address-line1/', AddressLine1DropdownView.as_view(), name='address_line1_dropdown'),
    path('dropdown/address-line2/', AddressLine2DropdownView.as_view(), name='address_line2_dropdown'),
    path('dropdown/city/', CityDropdownView.as_view(), name='city_dropdown'),
    path('dropdown/state/', StateDropdownView.as_view(), name='state_dropdown'),
    path('dropdown/zip/', ZipDropdownView.as_view(), name='zip_dropdown'),
    path('dropdown/email/', EmailDropdownView.as_view(), name='email_dropdown'),
    path('dropdown/phone-number/', PhoneNumberDropdownView.as_view(), name='phone_number_dropdown'),
    path('dropdown/race/', RaceDropdownView.as_view(), name='race_dropdown'),
    path('dropdown/ethnicity/', EthnicityDropdownView.as_view(), name='ethnicity_dropdown'),
    path('dropdown/entry-number/', EntryNumberDropdownView.as_view(), name='entry_number_dropdown'),
    path('dropdown/env/', EnvDropdownView.as_view(), name='env_dropdown'),
    path('dropdown/extract-flag/', ExtractFlagDropdownView.as_view(), name='extract_flag_dropdown'),
]
