from api_escola.models import Estudante, Curso, Matricula
from api_escola.serializers import (
    EstudanteSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListMatriculasEstudantesSerializer,
    EstudanteSerializerV2,
    ListMatriculaCursoSerializer,
)
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import (
    UserRateThrottle,
)
from api_escola.throttles import MatriculaAnonRateThrottle 

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by("id")
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome', 'cpf']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]
    http_method_names = ["get", "post"]

class ListMatriculaEstudante(generics.ListAPIView):
    serializer_class = ListMatriculasEstudantesSerializer

    def get_queryset(self):
        return Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by("id")

class ListMatriculaCurso(generics.ListAPIView):
    serializer_class = ListMatriculaCursoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by("id")
