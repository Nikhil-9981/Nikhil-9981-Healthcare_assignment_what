from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class Mapping(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctor_mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patient_mappings')
    reason = models.TextField(blank=True, help_text="Reason for mapping this doctor to the patient.")
    assigned_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} ↔ Dr. {self.doctor.name}"
