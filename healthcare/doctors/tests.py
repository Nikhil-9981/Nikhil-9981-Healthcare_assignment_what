from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Doctor

class DoctorTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="user2", password="pass123")
        response = self.client.post("/api/auth/login/", {
            "username": "user2", "password": "pass123"
        })
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_doctor(self):
        response = self.client.post("/api/doctors/", {
            "name": "Dr. Smith", "speciality": "Cardiology", "contact": "1234567890"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_doctors(self):
        Doctor.objects.create(name="Dr. Smith", speciality="Cardiology", contact="999")
        response = self.client.get("/api/doctors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
