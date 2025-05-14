
from api_escola.models import Estudante, Curso, Matricula
from api_escola.serializers import (
    EstudanteSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListMatriculasEstudantesSerializer,
    ListMatriculaCursoSerializer
)
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all()
    serializer_class = EstudanteSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListMatriculaEstudante(generics.ListAPIView):
    serializer_class = ListMatriculasEstudantesSerializer

    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk'])

class ListMatriculaCurso(generics.ListAPIView):
    serializer_class = ListMatriculaCursoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk'])
