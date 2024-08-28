# myapp/serializers.py
from rest_framework import serializers
from .models import Order, Specimen, Submitter, Patient

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class SpecimenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specimen
        fields = '__all__'

class SubmitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submitter
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
