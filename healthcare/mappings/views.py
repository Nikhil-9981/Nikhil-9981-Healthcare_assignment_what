from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.decorators import action

from .models import Mapping
from .serializers import MappingSerializer

class MappingViewSet(viewsets.ModelViewSet):
    queryset = Mapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as ve:
            return Response({"error": ve.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Mapping creation failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": f"Mapping update failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": f"Mapping deletion failed: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], url_path='doctors')
    def get_doctors_by_patient(self, request, pk=None):
        try:
            mappings = Mapping.objects.filter(patient__id=pk)
            if not mappings.exists():
                raise NotFound("No doctors found for this patient.")

            data = [
                {
                    "doctor_id": m.doctor.id,
                    "doctor_name": m.doctor.name,
                    "speciality": m.doctor.speciality
                } for m in mappings
            ]
            return Response(data)
        except NotFound as nf:
            return Response({"error": str(nf)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Failed to fetch doctors: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
