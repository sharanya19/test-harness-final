# myapp/serializers.py
from rest_framework import serializers
from .models import Order, Specimen, Submitter, Patient

class SpecimenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specimen
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    specimens = SpecimenSerializer(many=True, read_only=True)

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
