from django.test import TestCase
from api_escola.models import Estudante 


class ModelEstudanteTestCase(TestCase):
   # def test_falha(self):
       # self.fail('Teste falhou :(')
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'testedemodelo@gmail.com',
            cpf = '00825268508',
            data_nascimento = '1982-10-31',
            celular = '73 988040510'
        )

    def test_verifica_atributos_de_estudante(self):
        """ Teste que verifica os atributos do modelo de Estudante"""
        self.assertEqual(self.estudante.nome, 'Teste de Modelo')
        self.assertEqual(self.estudante.email, 'testedemodelo@gmail.com')
        self.assertEqual(self.estudante.cpf, '00825268508')
        self.assertEqual(str(self.estudante.data_nascimento), '1982-10-31')
        self.assertEqual(self.estudante.celular, '73 988040510')
