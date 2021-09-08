from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.enums import Choices
from django.contrib.auth.hashers import make_password

val_dent = False
val_pati = False
val_clin = False

class Speciality(models.Model):
    name = models.CharField(max_length=100)

class User(AbstractUser):
    is_dentist = models.BooleanField('dentist status', default=False)
    is_patient = models.BooleanField('patient status', default=False)
    is_clinic = models.BooleanField('clinic status', default=False)
    phone = models.CharField(max_length=12, null=True)
    email = models.EmailField(max_length=100,default=None)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    speciality = models.CharField(max_length=10)
    uic = models.CharField(max_length=20)
    def __str__(self):
        return self.firstname
    def save(self, *args, **kwargs):
        is_new = True if not self.id else False
        super(User, self).save(*args, **kwargs)
        if (is_new and self.is_clinic):
            clinic = Clinic(user=self, name = self.firstname, uic = self.uic)
            clinic.save()
        elif (is_new and self.is_patient):
            patient = Patient(user=self)
            patient.save()
        elif (is_new and self.is_dentist):
            dentist = Dentist(user=self, firstname = self.firstname, lastname = self.lastname)
            dentist.save()

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    uic = models.CharField(max_length=20)
    def __str__(self):
        return self.user.username



class Dentist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    clinics = models.ManyToManyField(Clinic)
    speciality = models.ManyToManyField(Speciality)
    avatar = models.ImageField(upload_to ='../Dentapp-frontend/src/assets/img/dentists/avatars/', default='../Dentapp-frontend/src/assets/img/dentists/avatars/avatar.jpeg')
    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to ='../Dentapp-frontend/src/assets/img/patients/avatars/', default='../Dentapp-frontend/src/assets/img/dentists/avatars/avatar.jpeg')
    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    STATUS = [
        ('initial','initial'),
        ('pending','pending'),
        ('confirmed','confirmed'),
        ('rejected','rejected'), 
        ('canceled','canceled')
    ]
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    dentist = models.ForeignKey(Dentist, on_delete=models.CASCADE)
    date_time = models.DateTimeField(unique=True, null=True, blank=True)
    is_urgent = models.BooleanField(default=False)
    status = models.CharField(max_length=100,choices=STATUS, default='initial')
    def __str__(self):
        return str(self.date_time) +' '+ self.dentist.user.email

class Report(models.Model):
    appointment = models.OneToOneField(Appointment,on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    def __str__(self):
        return self.appointment.patient.user.username

class Prescription(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    list = models.CharField(blank=True, max_length=100)
    def __str__(self):
        return self.report.appointment

class Finances(models.Model):
    clinic = models.OneToOneField(Clinic,on_delete=models.CASCADE)
    reports = models.ForeignKey(Report, on_delete=models.CASCADE, default=0)


