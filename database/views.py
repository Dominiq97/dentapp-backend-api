from typing import Generic
from .models import User, Appointment, Dentist, Report, Patient, Clinic
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics
from database.serializers import MyTokenObtainPairSerializer,UserSerializer, DentistSerializer, AppointmentSerializer, ReportSerializer, PatientSerializer,AppForDentistSerializer, ClinicSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from backend.settings import REST_FRAMEWORK
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.db.models import Q
from datetime import datetime, date, time, timedelta


def patient_list(request):
    if request.method == 'GET':
        patients = Patient.objects.all()
        
        patient_serializer = PatientSerializer(patients, many=True)
        return JsonResponse(patient_serializer.data, safe=False)
        # 'safe=False' for objects serialization


@api_view(['GET', 'POST', 'DELETE'])
def get_appointments_for_dentist(request,dentist_pk):
    if request.method == 'GET':
        dentist = Dentist.objects.get(pk = dentist_pk)
        apps = Appointment.objects.filter(dentist = dentist)
        
        app_serializer = AppForDentistSerializer(apps, many=True)
        return JsonResponse(app_serializer.data, safe=False)
        # 'safe=False' for objects serialization


@api_view(['GET', 'POST', 'DELETE'])
def dentist_list(request):
    if request.method == 'GET':
        dentists = Dentist.objects.all()
        
        dentist_serializer = DentistSerializer(dentists, many=True)
        return JsonResponse(dentist_serializer.data, safe=False)
        # 'safe=False' for objects serialization


@api_view(['GET', 'POST', 'DELETE'])
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)


@api_view(['GET'])
def dentist_detail(request, pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)

    except Dentist.DoesNotExist: 
        return JsonResponse({'message': 'The dentist does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        dentist_serializer = DentistSerializer(dentist) 
        return JsonResponse(dentist_serializer.data) 
 
@api_view(['GET'])
def patient_detail(request, pk):
    try: 
        user = User.objects.get(pk=pk)
        print(user)
        patient = Patient.objects.get(user = user) 
        print(patient)
    except Patient.DoesNotExist: 
        return JsonResponse({'message': 'The patient does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        patient_serializer = PatientSerializer(patient) 
        return JsonResponse(patient_serializer.data)

@api_view(['GET'])
def this_week_mon(request,pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)
        today = date.today() 
        monday = today - timedelta(today.weekday())
        apps = Appointment.objects.filter(dentist = dentist).filter(date_time__range=[str(monday)+"T00:00:00Z", str(monday)+"T23:59:59"]).filter(status='confirmed')
        app_serializer = AppForDentistSerializer(apps, many=True)
        return JsonResponse(app_serializer.data, safe=False)
    except Dentist.DoesNotExist: 
        return JsonResponse(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def this_week_tue(request,pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)
        today = date.today() 
        tuesday = today - timedelta(today.weekday())+ timedelta(days=1)
        apps = Appointment.objects.filter(dentist = dentist).filter(date_time__range=[str(tuesday)+"T00:00:00Z", str(tuesday)+"T23:59:59Z"]).filter(status='confirmed') 
        app_serializer = AppForDentistSerializer(apps, many=True)
        return JsonResponse(app_serializer.data, safe=False)
    except Dentist.DoesNotExist: 
        return JsonResponse(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def this_week_wed(request,pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)
        today = date.today() 
        wednesday = today - timedelta(today.weekday())+ timedelta(days=2)
        apps = Appointment.objects.filter(dentist = dentist).filter(date_time__range=[str(wednesday)+"T00:00:00Z", str(wednesday)+"T23:59:59"]).filter(status='confirmed')
        app_serializer = AppForDentistSerializer(apps, many=True)
        return JsonResponse(app_serializer.data, safe=False)
    except Dentist.DoesNotExist: 
        return JsonResponse(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def this_week_thu(request,pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)
        today = date.today() 
        thursday = today - timedelta(today.weekday())+timedelta(3)
        apps = Appointment.objects.filter(dentist = dentist).filter(date_time__range=[str(thursday)+"T00:00:00Z", str(thursday)+"T23:59:59"]).filter(status='confirmed')
        app_serializer = AppForDentistSerializer(apps, many=True)
        return JsonResponse(app_serializer.data, safe=False)
    except Dentist.DoesNotExist: 
        return JsonResponse(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def this_week_fri(request,pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)
        today = date.today() 
        friday = today - timedelta(today.weekday())+timedelta(4)
        apps = Appointment.objects.filter(dentist = dentist).filter(date_time__range=[str(friday)+"T00:00:00Z", str(friday)+"T23:59:59"]).filter(status='confirmed')
        app_serializer = AppForDentistSerializer(apps, many=True)
        return JsonResponse(app_serializer.data, safe=False)
    except Dentist.DoesNotExist: 
        return JsonResponse(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def that_week(request, pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)
        today = date.today() 
        start_this_week = today - timedelta(today.weekday())
        start_week = start_this_week
        start_next_week = start_this_week + timedelta(7)
        print(start_next_week)
        end_next_week = start_next_week + timedelta(7)
        print(end_next_week)
        apps = Appointment.objects.filter(dentist = dentist).filter(date_time__range=[str(start_next_week)+"T00:00:00Z", str(end_next_week)+"T23:59:59"]).filter(status='confirmed')
        
        app_serializer = AppForDentistSerializer(apps, many=True)
        return JsonResponse(app_serializer.data, safe=False)
    except Dentist.DoesNotExist: 
        return JsonResponse(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def get_dentist(request, pk):
    try: 
        user = User.objects.get(pk=pk)
        dentist = Dentist.objects.get(user = user) 
    except Dentist.DoesNotExist: 
        return JsonResponse({'message': 'The dentist does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        dentist_serializer = DentistSerializer(dentist) 
        return JsonResponse(dentist_serializer.data)


def to_appointments(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        
        appointment_serializer = AppointmentSerializer(appointments, many=True)
        return JsonResponse(appointment_serializer.data, safe=False)
 
    elif request.method == 'POST':
        appointment_data = JSONParser().parse(request)
        appointment_serializer = AppointmentSerializer(data=appointment_data)
        if appointment_serializer.is_valid():
            appointment_serializer.save()
            return JsonResponse(appointment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(appointment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def accept(request, pk):
    apps = Appointment.objects.all()
    if request.method == 'POST':
        for i in range(len(apps)):
            if (apps[i].pk == pk):
                apps[i].status='confirmed'
                apps[i].save()
        
        return HttpResponse("Successfully modified")


def decline(request, pk):
    apps = Appointment.objects.all()
    if request.method == 'POST':
        for i in range(len(apps)):
            if (apps[i].pk == pk):
                apps[i].status='rejected'
                apps[i].save()
        
        return HttpResponse("Successfully modified")

class DentistViewSet(viewsets.ModelViewSet):
    queryset = Dentist.objects.all()
    serializer_class = DentistSerializer
    permission_classes = [permissions.IsAuthenticated]

class IsPatient(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj.patient == request.user



class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = (IsPatient,)
    
    # Ensure a user sees only own Note objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Appointment.objects.filter(patient=user.pk)
        raise PermissionDenied()
        
    # Set user as owner of a Notes object.
    def perform_create(self, serializer):
        serializer.save(patient=self.request.user)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def get_today_appointments(request,pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)
        today = date.today() 
        apps = Appointment.objects.filter(dentist = dentist).filter(date_time__range=[str(today)+"T00:00:00Z", str(today)+"T23:59:59"]).filter(status='confirmed')
        app_serializer = AppForDentistSerializer(apps, many=True)
        return JsonResponse(app_serializer.data, safe=False)
    except Dentist.DoesNotExist: 
        return JsonResponse(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def get_pending_appointments(request,pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)
        apps = Appointment.objects.filter(dentist = dentist).filter(status='pending')
        app_serializer = AppForDentistSerializer(apps, many=True)
        return JsonResponse(app_serializer.data, safe=False)
    except Dentist.DoesNotExist: 
        return JsonResponse(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def get_patients_dentist(request,pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)
        apps = Appointment.objects.filter(dentist = dentist)
        list = []
        for app in apps:
            pat = app.patient
            list.append(pat)
        anotherList = []
        for i in list:
            if i not in anotherList:
                anotherList.append(i)
        patient_serializer = PatientSerializer(anotherList, many=True)
        return JsonResponse(patient_serializer.data, safe=False)
    except Dentist.DoesNotExist: 
        return JsonResponse(status=status.HTTP_404_NOT_FOUND) 

@api_view(['GET'])
def get_clinic(request, pk):
    try: 
        user = User.objects.get(pk=pk)
        clinic = Clinic.objects.get(user = user) 
    except Clinic.DoesNotExist: 
        return JsonResponse({'message': 'The clinic does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        clinic_serializer = ClinicSerializer(clinic) 
        return JsonResponse(clinic_serializer.data, safe=False)

@api_view(['GET'])
def get_clinic_obj(request, pk):
    try: 
        clinic = Clinic.objects.get(pk=pk)
    except Clinic.DoesNotExist: 
        return JsonResponse({'message': 'The clinic does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        clinic_serializer = ClinicSerializer(clinic) 
        return JsonResponse(clinic_serializer.data, safe=False)

@api_view(['GET'])
def get_patient_obj(request, pk):
    try: 
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist: 
        return JsonResponse({'message': 'The patient does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        patient_serializer = PatientSerializer(patient) 
        return JsonResponse(patient_serializer.data, safe=False)

@api_view(['GET'])
def get_dentist_obj(request, pk):
    try: 
        dentist = Dentist.objects.get(pk=pk)
    except Dentist.DoesNotExist: 
        return JsonResponse({'message': 'The dentist does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        dentist_serializer =DentistSerializer(dentist) 
        return JsonResponse(dentist_serializer.data, safe=False)



@api_view(['GET'])
def get_clinics(request):
    clinics = Clinic.objects.all()
    if request.method == 'GET': 
        clinic_serializer = ClinicSerializer(clinics, many=True) 
        return JsonResponse(clinic_serializer.data, safe=False)

@api_view(['GET'])
def get_dentists_of_clinic(request,pk):
    clinics = Clinic.objects.get(pk = pk)
    dentists = Dentist.objects.filter(clinics = clinics)
    if request.method == 'GET': 
        clinic_serializer = DentistSerializer(dentists, many=True) 
        return JsonResponse(clinic_serializer.data, safe=False)

@api_view(['GET'])
def get_appointments_of_clinic(request,pk):
    clinics = Clinic.objects.get(pk = pk)
    dentists = Dentist.objects.filter(clinics = clinics)
    list = []
    apps = Appointment.objects.all()
    for i in apps:
        for j in dentists:
            if i.dentist == j:
                list.append(i)
    if request.method == 'GET': 
        clinic_serializer = AppForDentistSerializer(list, many=True) 
        return JsonResponse(clinic_serializer.data, safe=False)

@api_view(['GET'])
def get_patients_of_clinic(request,pk):
    clinics = Clinic.objects.get(pk = pk)
    dentists = Dentist.objects.filter(clinics = clinics)
    list = []
    apps = Appointment.objects.all()
    for i in apps:
        for j in dentists:
            if i.dentist == j:
                list.append(i)
    listPatients = []
    for i in list:
        if i.patient not in listPatients:
            listPatients.append(i.patient)
    if request.method == 'GET': 
        clinic_serializer = PatientSerializer(listPatients, many=True) 
        return JsonResponse(clinic_serializer.data, safe=False)

@api_view(['GET'])
def get_patients_of_dentist(request,pk):
    dentist = Dentist.objects.get(pk = pk)
    apps = Appointment.objects.filter(dentist = dentist).filter(status='confirmed')
    list = []
    for i in apps:
        print(i)
        if i.patient not in list:
            list.append(i.patient)
    if request.method == 'GET': 
        clinic_serializer = PatientSerializer(list, many=True) 
        return JsonResponse(clinic_serializer.data, safe=False)




# class ReportViewSet(viewsets.ModelViewSet):
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializer
#     permission_classes = [permissions.IsAuthenticated]\


# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
#     permission_classes = [permissions.IsAuthenticated]

# from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# class ProfileView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request, format=None):
#         content = {
#            'user': str(request.user.username),  # `django.contrib.auth.User` instance.
#            'auth': str(request.auth),  # None
#         }
#         return Response(content)
    