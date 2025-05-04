from rest_framework import serializers
from .models import Mapping

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = '__all__'

    def validate(self, data):
        patient = data.get('patient')
        doctor = data.get('doctor')

        if not patient or not doctor:
            raise serializers.ValidationError("Both patient and doctor must be provided.")

        if Mapping.objects.filter(patient=patient, doctor=doctor).exists():
            raise serializers.ValidationError("This doctor is already assigned to this patient.")

        return data
