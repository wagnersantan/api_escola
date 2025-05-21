from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from api_escola.models import Estudante, Matricula
from api_escola.serializers import EstudanteSerializer, EstudanteSerializerV2, ListMatriculasEstudantesSerializer
from api_escola.serializers import (
    EstudanteSerializer,
    EstudanteSerializerV2,
    ListMatriculasEstudantesSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListMatriculaCursoSerializer
)

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by("id")
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class ListMatriculaEstudante(generics.ListAPIView):
    serializer_class = ListMatriculasEstudantesSerializer

    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")