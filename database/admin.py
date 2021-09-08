from django.contrib import admin
from .models import User, Dentist, Clinic,Patient, Appointment, Report, Finances, Prescription, Speciality

admin.site.register(User)
admin.site.register(Dentist)
admin.site.register(Clinic)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Report)
admin.site.register(Prescription)
admin.site.register(Finances)
admin.site.register(Speciality)