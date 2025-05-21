from rest_framework import viewsets, generics
from api_escola.models import Matricula
from api_escola.serializers import EstudanteSerializer, EstudanteSerializerV2, ListMatriculasEstudantesSerializer
from api_escola.serializers import (
    MatriculaSerializer,
    ListMatriculasEstudantesSerializer,
)
from rest_framework.throttling import UserRateThrottle
from api_escola.throttles import MatriculaAnonRateThrottle

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]

class ListMatriculaEstudante(generics.ListAPIView):
    serializer_class = ListMatriculasEstudantesSerializer

    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")
