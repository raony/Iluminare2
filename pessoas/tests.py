from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Pessoa

# Testes de funcao
class ListarPessoasTeste(TestCase):
    def test_retorna_200(self):
        response = self.client.get(reverse('pessoas-listar'))
        self.assertEqual(200, response.status_code)

    def test_retorna_lista(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        response = self.client.get(reverse('pessoas-listar'))
        self.assertContains(response, pessoa.nome)
        self.assertContains(response, pessoa.sobrenome)

    def test_template(self):
        response = self.client.get(reverse('pessoas-listar'))
        self.assertTemplateUsed(response, 'pessoas/pessoa_list.html')

    def test_link_para_adicionar(self):
        response = self.client.get(reverse('pessoas-listar'))
