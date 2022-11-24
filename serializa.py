from rest_framework import serializers
from .models import *
class DoctorSerializar(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'



class PatientSerializar(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


    