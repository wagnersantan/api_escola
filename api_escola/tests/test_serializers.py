from django.test import TestCase 
from api_escola.models import Estudante 
from api_escola.serializers import EstudanteSerializer 

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '00825268508',
            data_nascimento = '1982-10-31',
            celular = '73 988040510'
        )

        self.serializer_estudante = EstudanteSerializer(instance=self.estudante)
    
    def test_verifica_campos_serializados_de_estudante(self):
        """ Teste que verifica os campos que estão sendo serializados de estudante"""
        dados = self.serializer_estudante.data 
        self.assertEqual(set(dados.keys()),set(['id','nome','email','cpf','data_nascimento','celular']))
   
    def test_verifica_campos_serializados_de_estudante(self):
        """ Teste que verifica os campos que estão sendo serializados de estudante"""
        dados = self.serializer_estudante.data
        self.assertEqual(dados['nome'],self.estudante.nome)
        self.assertEqual(dados['email'],self.estudante.email)
        self.assertEqual(dados['cpf'],self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'], str(self.estudante.data_nascimento))
        self.assertEqual(dados['celular'], self.estudante.celular)
        
   