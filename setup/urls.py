from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# Importa os ViewSets e Views customizadas (de forma clara e sem duplicidade)
from api_escola.routers.estudantes_router import EstudanteViewSet, ListMatriculaEstudante
from api_escola.routers.cursos_router import CursoViewSet, ListMatriculaCurso
from api_escola.routers.matriculas_router import MatriculaViewSet

# Documentação automática
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API",
      default_version='v1',
      description="Documentação da API Escola",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    # Rotas customizadas para listar matrículas por estudante e curso
    path('estudantes/<int:pk>/matriculas/', ListMatriculaEstudante.as_view(), name='estudante-matriculas'),
    path('cursos/<int:pk>/matriculas/', ListMatriculaCurso.as_view(), name='curso-matriculas'),

    # Rotas da documentação automática (Swagger e Redoc)
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]

