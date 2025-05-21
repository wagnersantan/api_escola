from rest_framework import viewsets, generics
from api_escola.models import Curso, Matricula
from api_escola.serializers import EstudanteSerializer, EstudanteSerializerV2, ListMatriculasEstudantesSerializer
from api_escola.serializers import (
    CursoSerializer,
    ListMatriculaCursoSerializer,
)

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer

class ListMatriculaCurso(generics.ListAPIView):
    serializer_class = ListMatriculaCursoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
