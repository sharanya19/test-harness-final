from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import (Order, Specimen, SpecimenType, Submitter, Patient,  
    SpecimenTypeSNOMEDCode, 
    SourceDescription, 
    SpecimenSource, 
    SourceSNOMEDCode, Gender, City, State, Race, Ethnicity, Environment, District, OrderingPhysicianNPI, TestLocation, CollectionDate, CollectionTime)
from .serializers import (OrderSerializer, SpecimenSerializer, SpecimenTypeSerializer, SubmitterSerializer, PatientSerializer, SpecimenTypeSerializer, SpecimenTypeSNOMEDCodeSerializer, OrderingPhysicianNPISerializer, DistrictSerializer, TestLocationSerializer,
    SourceDescriptionSerializer, 
    SpecimenSourceSerializer, CollectionDateSerializer, CollectionTimeSerializer,
    SourceSNOMEDCodeSerializer,GenderSerializer, CitySerializer, StateSerializer, RaceSerializer, EthnicitySerializer, EnvironmentSerializer )

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params
        
        filter_conditions = Q()
        for param, value in query_params.items():
            if param in ['order_code', 'order_name', 'order_loinc_code', 'loinc_name', 'order_loinc_description']:
                filter_conditions &= Q(**{f"{param}__icontains": value})
        
        queryset = queryset.filter(filter_conditions)
        return queryset

class SpecimenViewSet(viewsets.ModelViewSet):
    queryset = Specimen.objects.all()
    serializer_class = SpecimenSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params
        
        filter_conditions = Q()
        for param, value in query_params.items():
            if param in ['specimen_id', 'specimen_type', 'specimen_type_snomed_code', 'source_description', 'specimen_source', 'source_snomed_code']:
                filter_conditions &= Q(**{f"{param}__icontains": value})
        
        queryset = queryset.filter(filter_conditions)
        return queryset

class SpecimenTypeViewSet(viewsets.ModelViewSet):
    queryset = SpecimenType.objects.all()
    serializer_class = SpecimenTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params
        
        filter_conditions = Q()
        for param, value in query_params.items():
            if param in ['specimen_type']:
                filter_conditions &= Q(**{f"{param}__icontains": value})
        
        queryset = queryset.filter(filter_conditions)
        return queryset

class SubmitterViewSet(viewsets.ModelViewSet):
    queryset = Submitter.objects.all()
    serializer_class = SubmitterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params
        
        filter_conditions = Q()
        for param, value in query_params.items():
            if param in ['submitter_code', 'district', 'orderingphysiciannpi', 'testlocation']:
                filter_conditions &= Q(**{f"{param}__icontains": value})
            elif param in ['collectiondate', 'collectiontime']:
                filter_conditions &= Q(**{param: value})
        
        queryset = queryset.filter(filter_conditions)
        return queryset

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params
        
        filter_conditions = Q()
        for param, value in query_params.items():
            if param in ['patient_first_name', 'patient_middle_name', 'patient_last_name', 'zip', 'email', 'phone_number', 'entry_number']:
                filter_conditions &= Q(**{f"{param}__icontains": value})
            elif param == 'patient_gender':
                filter_conditions &= Q(patient_gender__name=value)
            elif param == 'dob':
                filter_conditions &= Q(dob=value)
            elif param == 'extract_flag':
                filter_conditions &= Q(extract_flag=value)
            elif param == 'city':
                filter_conditions &= Q(city__name=value)
            elif param == 'state':
                filter_conditions &= Q(state__name=value)
            elif param == 'race':
                filter_conditions &= Q(race__name=value)
            elif param == 'ethnicity':
                filter_conditions &= Q(ethnicity__name=value)
            elif param == 'env':
                filter_conditions &= Q(env__name=value)
        
        queryset = queryset.filter(filter_conditions)
        return queryset

class SpecimenTypeViewSet(viewsets.ModelViewSet):
    queryset = SpecimenType.objects.all()
    serializer_class = SpecimenTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params

        filter_conditions = Q()
        for param, value in query_params.items():
            if param == 'specimen_type':
                filter_conditions &= Q(specimen_type__icontains=value)
            elif param == 'order':
                filter_conditions &= Q(order__order_code=value)

        queryset = queryset.filter(filter_conditions)
        return queryset

class SpecimenTypeSNOMEDCodeViewSet(viewsets.ModelViewSet):
    queryset = SpecimenTypeSNOMEDCode.objects.all()
    serializer_class = SpecimenTypeSNOMEDCodeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params

        filter_conditions = Q()
        for param, value in query_params.items():
            if param == 'specimen_type_snomed_code':
                filter_conditions &= Q(specimen_type_snomed_code__icontains=value)
            elif param == 'specimen_type':
                filter_conditions &= Q(specimen_type__specimen_type__icontains=value)

        queryset = queryset.filter(filter_conditions)
        return queryset

class SourceDescriptionViewSet(viewsets.ModelViewSet):
    queryset = SourceDescription.objects.all()
    serializer_class = SourceDescriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params

        filter_conditions = Q()
        for param, value in query_params.items():
            if param == 'source_description':
                filter_conditions &= Q(source_description__icontains=value)
            elif param == 'specimen_type_snomed_code':
                filter_conditions &= Q(specimen_type_snomed_code__specimen_type_snomed_code__icontains=value)

        queryset = queryset.filter(filter_conditions)
        return queryset

class SpecimenSourceViewSet(viewsets.ModelViewSet):
    queryset = SpecimenSource.objects.all()
    serializer_class = SpecimenSourceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params

        filter_conditions = Q()
        for param, value in query_params.items():
            if param == 'specimen_source':
                filter_conditions &= Q(specimen_source__icontains=value)
            elif param == 'source_description':
                filter_conditions &= Q(source_description__source_description__icontains=value)

        queryset = queryset.filter(filter_conditions)
        return queryset

class SourceSNOMEDCodeViewSet(viewsets.ModelViewSet):
    queryset = SourceSNOMEDCode.objects.all()
    serializer_class = SourceSNOMEDCodeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params

        filter_conditions = Q()
        for param, value in query_params.items():
            if param == 'source_snomed_code':
                filter_conditions &= Q(source_snomed_code__icontains=value)
            elif param == 'specimen_source':
                filter_conditions &= Q(specimen_source__specimen_source__icontains=value)

        queryset = queryset.filter(filter_conditions)
        return queryset
    

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticated]

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [IsAuthenticated]

class RaceViewSet(viewsets.ModelViewSet):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    permission_classes = [IsAuthenticated]

class EthnicityViewSet(viewsets.ModelViewSet):
    queryset = Ethnicity.objects.all()
    serializer_class = EthnicitySerializer
    permission_classes = [IsAuthenticated]

class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [IsAuthenticated]

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes = [IsAuthenticated] 


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    permission_classes = [IsAuthenticated]

class TestLocationViewSet(viewsets.ModelViewSet):
    queryset = TestLocation.objects.all()
    serializer_class = TestLocationSerializer
    permission_classes = [IsAuthenticated]

class OrderingPhysicianNPIViewSet(viewsets.ModelViewSet):
    queryset = OrderingPhysicianNPI.objects.all()
    serializer_class = OrderingPhysicianNPISerializer
    permission_classes = [IsAuthenticated]

class CollectionDateViewSet(viewsets.ModelViewSet):
    queryset = CollectionDate.objects.all()
    serializer_class = CollectionDateSerializer
    permission_classes = [IsAuthenticated]

class CollectionTimeViewSet(viewsets.ModelViewSet):
    queryset = CollectionTime.objects.all()
    serializer_class = CollectionTimeSerializer 
    permission_classes = [IsAuthenticated]   

class SubmitterViewSet(viewsets.ModelViewSet):
    queryset = Submitter.objects.all()
    serializer_class = SubmitterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        query_params = self.request.query_params
        
        filter_conditions = Q()
        for param, value in query_params.items():
            if param in ['submitter_code']:
                filter_conditions &= Q(**{f"{param}__icontains": value})
            elif param == 'district':
                filter_conditions &= Q(district__name__icontains=value)
            elif param == 'test_location':
                filter_conditions &= Q(test_location__location_name__icontains=value)
            elif param == 'ordering_physician_npi':
                filter_conditions &= Q(ordering_physician_npi__npi_code__icontains=value)
            elif param in ['collection_date', 'collection_time']:
                filter_conditions &= Q(**{param: value})
        
        queryset = queryset.filter(filter_conditions)
        return queryset