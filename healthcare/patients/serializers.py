from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ['owner']

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        if value > 130:
            raise serializers.ValidationError("Please enter a valid age.")
        return value

    def validate_name(self, value):
        if not value.replace(' ', '').isalpha():
            raise serializers.ValidationError("Name must contain only alphabets.")
        return value

    def validate(self, attrs):
        # Example object-level validation (custom business rules can be added here)
        name = attrs.get('name', '')
        if 'test' in name.lower():
            raise serializers.ValidationError("Name cannot contain 'test'.")
        return attrs
