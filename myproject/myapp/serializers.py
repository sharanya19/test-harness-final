from rest_framework import serializers
from .models import (
    Order, Specimen, Submitter, Patient, 
    SpecimenType, SpecimenTypeSNOMEDCode, SourceDescription, SpecimenSource, SourceSNOMEDCode
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

class SubmitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submitter
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
