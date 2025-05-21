from django.contrib import admin

from .estudantes_admin import Estudante, Estudantes
from .cursos_admin import Curso, Cursos
from .matriculas_admin import Matricula, Matriculas

admin.site.register(Estudante, Estudantes)
admin.site.register(Curso, Cursos)
admin.site.register(Matricula, Matriculas)