from rest_framework import serializers
from api_escola.models import Matricula

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListMatriculasEstudantesSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListMatriculaCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['estudante_nome', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
