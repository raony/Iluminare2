from django.test import TestCase

from django_webtest import WebTest
from django.core.urlresolvers import reverse
from datetime import datetime

from pessoas.models import Pessoa
from salas.models import Sala
from .models import Tratamento, Sessao

# Testes de função
class AdicionarTratamentoPessoaTeste(WebTest):
    def test_adicionar_tratamento_a_pessoa(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        tela_adicionar = self.app.get(reverse('tratamentos-pessoa-adicionar', args=[pessoa.pk,]))
        self.assertEquals(pessoa, tela_adicionar.context['form'].initial['paciente'])

    def test_link_adicionar_sessao(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        tratamento = Tratamento.objects.create(paciente=pessoa, inicio=datetime.now().date(), ativo=True)

        tela_tratamento = self.app.get(reverse('tratamentos-visualizar', args=[tratamento.pk, ]))
        tela_adicionar_sessao = tela_tratamento.click('Adicionar sessao', index=0)

        self.assertEquals(200, tela_adicionar_sessao.status_code)
        self.assertEquals(reverse('sessoes-adicionar', args=[tratamento.pk,]), tela_adicionar_sessao.request.path)

class ListarTratamentoTeste(WebTest):
    def test_link_adicionar_tratamento(self):
        listagem = self.app.get(reverse('tratamentos-listar'))
        adicionar = listagem.click('Adicionar', index=0)

        self.assertEquals(200, adicionar.status_code)
        self.assertEquals(reverse('tratamentos-adicionar'), adicionar.request.path)

class DetalharTratamentoTeste(WebTest):
    def test_adicionar_sessao(self):
        sala = Sala.objects.create(nome='sala teste')
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        tratamento = Tratamento.objects.create(paciente=pessoa, inicio=datetime(2015,1,1).date(), ativo=True)
        tela_detalhar = self.app.get(reverse('tratamentos-visualizar', args=[tratamento.pk,]))
        tela_adicionar_sessao = tela_detalhar.click('Adicionar')
        tela_adicionar_sessao.form['sala'] = sala.pk
        tela_adicionar_sessao.form['quantidade'] = 12
        resultado = tela_adicionar_sessao.form.submit().follow()
        self.assertEquals(1, tratamento.sessao_set.all().count())
        self.assertEquals(reverse('tratamentos-visualizar', args=[tratamento.pk,]), resultado.request.path)
        self.assertContains(resultado, sala.nome)
        self.assertContains(resultado, '<td>12</td>')

    def test_remover_sessao(self):
        sala = Sala.objects.create(nome='sala teste')
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        tratamento = Tratamento.objects.create(paciente=pessoa, inicio=datetime(2015,1,1).date(), ativo=True)
        sessao = Sessao.objects.create(sala=sala, tratamento=tratamento, quantidade=12)

        tela_detalhar = self.app.get(reverse('tratamentos-visualizar', args=[tratamento.pk, ]))
        resultado = tela_detalhar.form.submit().follow()
        self.assertEquals(0, tratamento.sessao_set.all().count())
        self.assertNotContains(resultado, sala.nome)
        self.assertNotContains(resultado, '<td>12</td>')

