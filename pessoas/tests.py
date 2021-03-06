from django.test import TestCase

from django_webtest import WebTest
from django.core.urlresolvers import reverse
from datetime import datetime

from .models import Pessoa
from tratamento.models import Tratamento

# Testes unitarios
class PessoaTeste(TestCase):
    def test_tratamento_atual_sera_o_mais_recente_ativo(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        tratamento_antigo = Tratamento.objects.create(paciente=pessoa, inicio=datetime(2015,5,4), ativo=True)
        tratamento_atual = Tratamento.objects.create(paciente=pessoa, inicio=datetime(2016, 5, 4), ativo=True)
        tratamento_inativo = Tratamento.objects.create(paciente=pessoa, inicio=datetime(2016, 6, 4), ativo=False)

        self.assertEquals(tratamento_atual, pessoa.tratamento)

    def test_tratamento_inativo(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        tratamento_inativo = Tratamento.objects.create(paciente=pessoa, inicio=datetime(2016, 6, 4), ativo=False)

        self.assertEquals(None, pessoa.tratamento)

    def test_tratamento_nao_existente(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')

        self.assertEquals(None, pessoa.tratamento)

    def test_nome_capital(self):
        pessoa = Pessoa.objects.create(nome='teste rodrigo', sobrenome='teste2')
        self.assertEquals('Teste Rodrigo', pessoa.nome)

    def test_sobrenome_capital(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2 silva')
        self.assertEquals('Teste2 Silva', pessoa.sobrenome)

    def test_remover_espacos_nome(self):
        pessoa = Pessoa.objects.create(nome=' \t  luiz   \t carlos\tdaniel  \t', sobrenome='  \t romero  \t silva\tfilho  \t  ')
        self.assertEquals('Luiz Carlos Daniel', pessoa.nome)
        self.assertEquals('Romero Silva Filho', pessoa.sobrenome)

    def test_nome_completo(self):
        pessoa = Pessoa.objects.create(nome='luiz carlos', sobrenome='romero filho')
        self.assertEquals('luiz carlos romero filho', pessoa.nome_completo)

    def test_nome_completo_acento(self):
        pessoa = Pessoa.objects.create(nome='Luís carlos', sobrenome='Gonçalves')
        self.assertEquals('luis carlos goncalves', pessoa.nome_completo)

    def test_buscar_pessoa_por_nome(self):
        pessoa1 = Pessoa.objects.create(nome='luiz carlos', sobrenome='romero filho')
        pessoa2 = Pessoa.objects.create(nome='carlos', sobrenome='gonçalves romeu dos santos')

        self.assertEquals(2, len(Pessoa.objects.filter_by_name('ca')))
        self.assertEquals(2, len(Pessoa.objects.filter_by_name('car')))
        self.assertEquals(2, len(Pessoa.objects.filter_by_name('rome')))
        self.assertEquals(1, len(Pessoa.objects.filter_by_name('romero')))

    def test_buscar_pessoa_por_nome_duas_palavras(self):
        pessoa1 = Pessoa.objects.create(nome='luiz carlos', sobrenome='romero filho')
        pessoa2 = Pessoa.objects.create(nome='carlos', sobrenome='gonçalves romeu dos santos')

        self.assertEquals(1, len(Pessoa.objects.filter_by_name('carlos filho')))
        self.assertEquals(1, len(Pessoa.objects.filter_by_name('carlos goncalves')))
        self.assertEquals(1, len(Pessoa.objects.filter_by_name('carlos gonçalves')))
        self.assertEquals(1, len(Pessoa.objects.filter_by_name('ca go')))

# Testes de funcao
class ListarPessoasTeste(WebTest):

    def retorna_lista(self, html):
        return html.tbody.find_all('tr')

    def test_retorna_200(self):
        response = self.app.get(reverse('pessoas-listar'))
        self.assertEqual(200, response.status_code)

    def test_retorna_lista(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        response = self.app.get(reverse('pessoas-listar'))
        self.assertEqual(1, len(self.retorna_lista(response.html)))
        self.assertContains(response, pessoa.nome)
        self.assertContains(response, pessoa.sobrenome)

    def test_link_para_adicionar(self):
        listar = self.app.get(reverse('pessoas-listar'))
        adicionar = listar.click('Adicionar', index=0)
        self.assertEquals(200, adicionar.status_code)
        self.assertEquals(reverse('pessoas-adicionar'), adicionar.request.path)


class AdicionarPessoasTeste(WebTest):
    def test_retorna_200_get(self):
        response = self.app.get(reverse('pessoas-adicionar'))
        self.assertEqual(200, response.status_code)

    def test_salva_quando_submete(self):
        adicionar = self.app.get(reverse('pessoas-adicionar'))
        adicionar.form['nome'] = 'teste'
        adicionar.form['sobrenome'] = 'testesobrenome'
        adicionar.form.submit()
        self.assertTrue(Pessoa.objects.filter(nome__iexact='teste').exists())

    def test_retorna_pra_listagem_apos_salvar(self):
        adicionar = self.app.get(reverse('pessoas-adicionar'))
        adicionar.form['nome'] = 'teste'
        adicionar.form['sobrenome'] = 'testesobrenome'
        response = adicionar.form.submit()
        self.assertRedirects(response, reverse("pessoas-listar"))

    def test_submissao_com_erro(self):
        adicionar = self.app.get(reverse('pessoas-adicionar'))
        adicionar.form['nome'] = 'teste'
        response = adicionar.form.submit()
        self.assertFormError(response, 'form', 'sobrenome', 'Este campo é obrigatório.')

class VisualizarPessoasTeste(WebTest):
    def test_retorna_200_get(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        response = self.app.get(reverse('pessoas-visualizar', args=[pessoa.pk,]))
        self.assertContains(response, pessoa.nome)
        self.assertContains(response, pessoa.sobrenome)

    def test_link_atualizar(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        visualizar = self.app.get(reverse('pessoas-visualizar', args=[pessoa.pk, ]))
        atualizar = visualizar.click('Atualizar', index=0)
        self.assertEquals(200, atualizar.status_code)
        self.assertEquals(reverse('pessoas-atualizar', args=[pessoa.pk,]), atualizar.request.path)

    def test_link_tratamento(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        tratamento = Tratamento.objects.create(paciente=pessoa, inicio=datetime.today())

        visualizar = self.app.get(reverse('pessoas-visualizar', args=[pessoa.pk, ]))
        tratamento_visualizar = visualizar.click('Tratamento', index=1) #o primeiro link é o da navbar

        self.assertEquals(200, tratamento_visualizar.status_code)
        self.assertEquals(reverse('tratamentos-visualizar', args=[tratamento.pk,]),
                          tratamento_visualizar.request.path)

    def test_link_novo_tratamento(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')

        visualizar = self.app.get(reverse('pessoas-visualizar', args=[pessoa.pk, ]))
        tratamento_adicionar = visualizar.click('Novo Tratamento', index=0)

        self.assertEquals(200, tratamento_adicionar.status_code)
        self.assertEquals(reverse('tratamentos-pessoa-adicionar', args=[pessoa.pk, ]),
                          tratamento_adicionar.request.path)

class AtualizarPessoasTeste(WebTest):
    def test_atualizar(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        atualizar = self.app.get(reverse('pessoas-atualizar', args=[pessoa.pk,]))
        atualizar.form['nome'] = 'novo nome'
        resultado = atualizar.form.submit()
        self.assertRedirects(resultado, reverse('pessoas-visualizar', args=[pessoa.pk,]))
        self.assertEqual('Novo Nome', Pessoa.objects.get(pk=pessoa.pk).nome)

