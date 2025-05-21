from django.db import models
from .estudante import Estudante
from .curso import Curso

PERIODO = (
    ('M', 'Matutino'),
    ('V', 'Vespertino'),
    ('N', 'Noturno'),
)

class Matricula(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')
