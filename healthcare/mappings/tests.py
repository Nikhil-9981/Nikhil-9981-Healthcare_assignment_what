from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from patients.models import Patient
from doctors.models import Doctor
from .models import Mapping

class MappingTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user3", password="pass123")
        login = self.client.post("/api/auth/login/", {
            "username": "user3", "password": "pass123"
        })
        self.token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.patient = Patient.objects.create(owner=self.user, name="P1", age=30)
        self.doctor = Doctor.objects.create(name="D1", speciality="Neuro", contact="123")

    def test_create_mapping(self):
        response = self.client.post("/api/mappings/", {
            "patient": self.patient.id,
            "doctor": self.doctor.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_mappings(self):
        Mapping.objects.create(patient=self.patient, doctor=self.doctor)
        response = self.client.get("/api/mappings/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_doctors_for_patient(self):
        Mapping.objects.create(patient=self.patient, doctor=self.doctor)
        response = self.client.get(f"/api/mappings/{self.patient.id}/doctors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_mapping(self):
        mapping = Mapping.objects.create(patient=self.patient, doctor=self.doctor)
        response = self.client.delete(f"/api/mappings/{mapping.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
