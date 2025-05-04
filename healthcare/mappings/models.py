from django.db import models

# Create your models here.
class Mapping(models.Model):
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE)
    assigned_on = models.DateTimeField(auto_now_add=True)
