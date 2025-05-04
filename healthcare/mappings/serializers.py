from rest_framework import serializers
from .models import Mapping

class MappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapping
        fields = '__all__'

    def validate(self, data):
        if Mapping.objects.filter(patient=data['patient'], doctor=data['doctor']).exists():
            raise serializers.ValidationError("This doctor is already assigned to this patient.")
        return data
