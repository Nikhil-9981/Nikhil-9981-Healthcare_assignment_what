from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    contact = models.CharField(max_length=15)
    address = models.TextField(blank=True)
    medical_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
