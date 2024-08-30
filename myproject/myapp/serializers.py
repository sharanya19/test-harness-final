from rest_framework import serializers
from .models import (
    Order, Specimen, Submitter, Patient, 
    SpecimenType, SpecimenTypeSNOMEDCode, SourceDescription, SpecimenSource, SourceSNOMEDCode, City, State, Race, Ethnicity, Environment, Gender, OrderingPhysicianNPI, District, TestLocation
)

class SpecimenTypeSNOMEDCodeSerializer(serializers.ModelSerializer):
    specimen_type = serializers.StringRelatedField()

    class Meta:
        model = SpecimenTypeSNOMEDCode
        fields = '__all__'

class SourceDescriptionSerializer(serializers.ModelSerializer):
    specimen_type_snomed_code = SpecimenTypeSNOMEDCodeSerializer(read_only=True)

    class Meta:
        model = SourceDescription
        fields = '__all__'

class SpecimenSourceSerializer(serializers.ModelSerializer):
    source_description = SourceDescriptionSerializer(read_only=True)

    class Meta:
        model = SpecimenSource
        fields = '__all__'

class SourceSNOMEDCodeSerializer(serializers.ModelSerializer):
    specimen_source = SpecimenSourceSerializer(read_only=True)

    class Meta:
        model = SourceSNOMEDCode
        fields = '__all__'



class SpecimenTypeSerializer(serializers.ModelSerializer):
    snomed_codes = SpecimenTypeSNOMEDCodeSerializer(many=True, read_only=True)
    order = serializers.StringRelatedField()

    class Meta:
        model = SpecimenType
        fields = '__all__'

class SpecimenSerializer(serializers.ModelSerializer):
    specimen_type = SpecimenTypeSerializer(read_only=True)
    specimen_type_snomed_code = SpecimenTypeSNOMEDCodeSerializer(read_only=True)
    source_description = SourceDescriptionSerializer(read_only=True)
    specimen_source = SpecimenSourceSerializer(read_only=True)
    source_snomed_code = SourceSNOMEDCodeSerializer(read_only=True)

    class Meta:
        model = Specimen
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    specimens = SpecimenSerializer(many=True, read_only=True)
    specimen_types = SpecimenTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class TestLocationSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)  # Nested serialization

    class Meta:
        model = TestLocation
        fields = '__all__'

class OrderingPhysicianNPISerializer(serializers.ModelSerializer):
    test_location = TestLocationSerializer(read_only=True)  # Nested serialization

    class Meta:
        model = OrderingPhysicianNPI
        fields = '__all__'

class SubmitterSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(read_only=True)  # Nested serialization
    test_location = TestLocationSerializer(read_only=True)  # Nested serialization
    ordering_physician_npi = OrderingPhysicianNPISerializer(read_only=True)  # Nested serialization

    class Meta:
        model = Submitter
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'

class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnicity
        fields = '__all__'

class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    state = StateSerializer()
    race = RaceSerializer()
    ethnicity = EthnicitySerializer()
    env = EnvironmentSerializer()
    patient_gender = GenderSerializer()

    class Meta:
        model = Patient
        fields = '__all__'

    def create(self, validated_data):
        city_data = validated_data.pop('city', None)
        state_data = validated_data.pop('state', None)
        race_data = validated_data.pop('race', None)
        ethnicity_data = validated_data.pop('ethnicity', None)
        env_data = validated_data.pop('env', None)
        gender_data = validated_data.pop('patient_gender', None)

        city = City.objects.get_or_create(**city_data)[0] if city_data else None
        state = State.objects.get_or_create(**state_data)[0] if state_data else None
        race = Race.objects.get_or_create(**race_data)[0] if race_data else None
        ethnicity = Ethnicity.objects.get_or_create(**ethnicity_data)[0] if ethnicity_data else None
        env = Environment.objects.get_or_create(**env_data)[0] if env_data else None
        gender = Gender.objects.get_or_create(**gender_data)[0] if gender_data else None

        patient = Patient.objects.create(
            city=city,
            state=state,
            race=race,
            ethnicity=ethnicity,
            env=env,
            patient_gender=gender,
            **validated_data
        )
        return patient