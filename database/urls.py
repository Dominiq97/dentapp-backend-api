from rest_framework import routers
from django.urls import path, include
from database import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

router = routers.DefaultRouter()


urlpatterns = [
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),
    path('api/appointments/', views.to_appointments),
    path('api/dentists/', views.dentist_list),
    path('api/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('api/booking/dentist/<int:pk>', views.dentist_detail),
    path('api/patients/', views.patient_list),
    path('api/appointments/<int:dentist_pk>', views.get_appointments_for_dentist),
    path('api/users/', views.users_list),
    path('api/appointment/accept/<int:pk>', views.accept),
    path('api/appointment/decline/<int:pk>', views.decline),
    path('api/appointment/this_week_mon/<int:pk>', views.this_week_mon),
    path('api/appointment/this_week_tue/<int:pk>', views.this_week_tue),
    path('api/appointment/this_week_wed/<int:pk>', views.this_week_wed),
    path('api/appointment/this_week_thu/<int:pk>', views.this_week_thu),
    path('api/appointment/this_week_fri/<int:pk>', views.this_week_fri),
    path('api/appointment/that_week/<int:pk>', views.that_week),
    path('api/appointments/today/<int:pk>',views.get_today_appointments),
    path('api/appointments/get_patients_dentist/<int:pk>',views.get_patients_dentist),
    path('api/appointments/pending/<int:pk>',views.get_pending_appointments),
    # GET Object AFTER USER ID
    path('api/patients/<int:pk>', views.patient_detail),
    path('api/dentists/<int:pk>', views.get_dentist),
    path('api/clinics/<int:pk>', views.get_clinic),
    #------------------------------------------------
    # GET Object AFTER Its id
    path('api/patient/<int:pk>', views.get_patient_obj),
    path('api/dentist/<int:pk>', views.get_dentist_obj),
    path('api/clinic/<int:pk>', views.get_clinic_obj),
    #------------------------------------------------
    path('api/all_clinics',views.get_clinics),
    path('api/dentists_of_clinic/<int:pk>', views.get_dentists_of_clinic),
    path('api/appointments_of_clinic/<int:pk>',views.get_appointments_of_clinic),
    path('api/patients_of_clinic/<int:pk>',views.get_patients_of_clinic),
    path('api/patients_of_dentist/<int:pk>', views.get_patients_of_dentist)

]