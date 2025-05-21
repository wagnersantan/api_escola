from django.contrib import admin
from api_escola.models import Estudante

class Estudantes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular')
    list_display_links = ('id', 'nome')
    list_per_page = 20
    search_fields = ('nome', 'cpf')
    ordering = ('nome',)

admin.site.register(Estudante, Estudantes)
