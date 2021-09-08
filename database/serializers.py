from .models import Appointment, Dentist, Patient, Report, Clinic, Speciality
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'is_dentist', 'is_clinic', 'is_patient','pk']
    def validate_password(self, value: str) -> str:
        return make_password(value)

class UsrSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'is_dentist', 'is_clinic', 'is_patient','pk']

class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['city', 'address', 'name','pk','user','uic']
        depth = 1

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date_time','patient', 'dentist','status', 'pk']

class AppForDentistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['date_time','patient', 'dentist','status','is_urgent', 'pk']
        depth=2

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = ['name']
        
class DentistSerializer(serializers.ModelSerializer):
    clinics = ClinicSerializer(many=True)
    speciality = SpecialitySerializer(many=True)
    class Meta:
        model = Dentist
        fields = ['firstname','lastname','degree','clinics','user', 'speciality','pk','avatar']
        depth = 1

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['is_dentist'] = self.user.is_dentist
        data['is_patient'] = self.user.is_patient
        data['is_clinic'] = self.user.is_clinic
        data['pk'] = self.user.pk
        return data

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['price','appointment']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['pk','user','avatar']
        depth = 1
