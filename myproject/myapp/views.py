# myapp/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from .models import Order, Specimen, Submitter, Patient
from .serializers import OrderSerializer, SpecimenSerializer, SubmitterSerializer, PatientSerializer

# ViewSets for CRUD operations
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class SpecimenViewSet(viewsets.ModelViewSet):
    queryset = Specimen.objects.all()
    serializer_class = SpecimenSerializer
    permission_classes = [IsAuthenticated]

class SubmitterViewSet(viewsets.ModelViewSet):
    queryset = Submitter.objects.all()
    serializer_class = SubmitterSerializer
    permission_classes = [IsAuthenticated]

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

# Dropdown views for Specimen fields
class SpecimenTypeDropdownView(APIView):
    def get(self, request):
        order_code = request.query_params.get('order_code')
        specimens = Specimen.objects.filter(order__order_code=order_code)
        specimen_types = specimens.values_list('specimen_type', flat=True).distinct()
        return Response(list(specimen_types))

class SpecimenTypeSnomedCodeDropdownView(APIView):
    def get(self, request):
        specimen_type = request.query_params.get('specimen_type')
        specimens = Specimen.objects.filter(specimen_type=specimen_type)
        snomed_codes = specimens.values_list('specimen_type_snomed_code', flat=True).distinct()
        return Response(list(snomed_codes))

class SourceDescriptionDropdownView(APIView):
    def get(self, request):
        specimen_type_snomed_code = request.query_params.get('specimen_type_snomed_code')
        specimens = Specimen.objects.filter(specimen_type_snomed_code=specimen_type_snomed_code)
        source_descriptions = specimens.values_list('source_description', flat=True).distinct()
        return Response(list(source_descriptions))

class SpecimenSourceDropdownView(APIView):
    def get(self, request):
        source_description = request.query_params.get('source_description')
        specimens = Specimen.objects.filter(source_description=source_description)
        specimen_sources = specimens.values_list('specimen_source', flat=True).distinct()
        return Response(list(specimen_sources))

class SourceSnomedCodeDropdownView(APIView):
    def get(self, request):
        specimen_source = request.query_params.get('specimen_source')
        specimens = Specimen.objects.filter(specimen_source=specimen_source)
        source_snomed_codes = specimens.values_list('source_snomed_code', flat=True).distinct()
        return Response(list(source_snomed_codes))

# Dropdown views for Submitter fields
class DistrictDropdownView(APIView):
    def get(self, request):
        submitters = Submitter.objects.all()
        districts = submitters.values_list('district', flat=True).distinct()
        return Response(list(districts))

class PhysicianNpiDropdownView(APIView):
    def get(self, request):
        submitters = Submitter.objects.all()
        physician_npis = submitters.values_list('orderingphysiciannpi', flat=True).distinct()
        return Response(list(physician_npis))

class CollectionDateDropdownView(APIView):
    def get(self, request):
        submitters = Submitter.objects.all()
        collection_dates = submitters.values_list('collectiondate', flat=True).distinct()
        return Response(list(collection_dates))

class CollectionTimeDropdownView(APIView):
    def get(self, request):
        submitters = Submitter.objects.all()
        collection_times = submitters.values_list('collectiontime', flat=True).distinct()
        return Response(list(collection_times))

class TestLocationDropdownView(APIView):
    def get(self, request):
        submitters = Submitter.objects.all()
        test_locations = submitters.values_list('testlocation', flat=True).distinct()
        return Response(list(test_locations))

# Dropdown views for Patient fields
class PatientFirstNameDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        first_names = patients.values_list('patient_first_name', flat=True).distinct()
        return Response(list(first_names))

class PatientMiddleNameDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        middle_names = patients.values_list('patient_middle_name', flat=True).distinct()
        return Response(list(middle_names))

class PatientLastNameDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        last_names = patients.values_list('patient_last_name', flat=True).distinct()
        return Response(list(last_names))

class PatientGenderDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        genders = patients.values_list('patient_gender', flat=True).distinct()
        return Response(list(genders))

class DobDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        dobs = patients.values_list('dob', flat=True).distinct()
        return Response(list(dobs))

class AddressLine1DropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        addresses_line1 = patients.values_list('address_line1', flat=True).distinct()
        return Response(list(addresses_line1))

class AddressLine2DropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        addresses_line2 = patients.values_list('address_line2', flat=True).distinct()
        return Response(list(addresses_line2))

class CityDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        cities = patients.values_list('city', flat=True).distinct()
        return Response(list(cities))

class StateDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        states = patients.values_list('state', flat=True).distinct()
        return Response(list(states))

class ZipDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        zips = patients.values_list('zip', flat=True).distinct()
        return Response(list(zips))

class EmailDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        emails = patients.values_list('email', flat=True).distinct()
        return Response(list(emails))

class PhoneNumberDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        phone_numbers = patients.values_list('phone_number', flat=True).distinct()
        return Response(list(phone_numbers))

class RaceDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        races = patients.values_list('race', flat=True).distinct()
        return Response(list(races))

class EthnicityDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        ethnicities = patients.values_list('ethnicity', flat=True).distinct()
        return Response(list(ethnicities))

class EntryNumberDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        entry_numbers = patients.values_list('entry_number', flat=True).distinct()
        return Response(list(entry_numbers))

class EnvDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        envs = patients.values_list('env', flat=True).distinct()
        return Response(list(envs))

class ExtractFlagDropdownView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        extract_flags = patients.values_list('extract_flag', flat=True).distinct()
        return Response(list(extract_flags))
