from rest_framework import serializers
from api_escola.models import Estudante, Curso

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'