from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Patient

class PatientTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user1", password="pass123")
        response = self.client.post("/api/auth/login/", {
            "username": "user1", "password": "pass123"
        })
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_patient(self):
        response = self.client.post("/api/patients/", {
            "name": "John Doe", "age": 45, "medical_history": "Diabetes"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_patients(self):
        # ✅ Create a test patient
        Patient.objects.create(owner=self.user, name="Test", age=50, medical_history="None")
        
        # ✅ Now get the list
        response = self.client.get("/api/patients/")
        print("Response Data:", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
