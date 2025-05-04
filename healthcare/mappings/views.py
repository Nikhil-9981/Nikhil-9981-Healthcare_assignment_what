from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Mapping
from .serializers import MappingSerializer
 
from rest_framework.decorators import action
from rest_framework.response import Response

class MappingViewSet(viewsets.ModelViewSet):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='doctors')
    def get_doctors_by_patient(self, request, pk=None):
        mappings = Mapping.objects.filter(patient__id=pk)
        data = [
            {
                "doctor_id": m.doctor.id,
                "doctor_name": m.doctor.name,
                "speciality": m.doctor.speciality
            } for m in mappings
        ]
        return Response(data)
