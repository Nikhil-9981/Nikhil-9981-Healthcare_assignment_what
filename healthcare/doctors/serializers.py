from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_name(self, value):
        if not value.replace(' ', '').isalpha():
            raise serializers.ValidationError("Name must only contain alphabetic characters.")
        return value

    def validate_speciality(self, value):
        if not value.strip():
            raise serializers.ValidationError("Speciality field cannot be empty.")
        return value

    def validate_contact(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact must contain only digits.")
        if len(value) < 10 or len(value) > 15:
            raise serializers.ValidationError("Contact must be between 10 to 15 digits.")
        return value
