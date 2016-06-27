from django_webtest import WebTest
from django.core.urlresolvers import reverse

from .models import Pessoa

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
        self.assertTrue(Pessoa.objects.filter(nome='teste').exists())

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

class AtualizarPessoasTeste(WebTest):
    def test_atualizar(self):
        pessoa = Pessoa.objects.create(nome='teste', sobrenome='teste2')
        atualizar = self.app.get(reverse('pessoas-atualizar', args=[pessoa.pk,]))
        atualizar.form['nome'] = 'novo nome'
        resultado = atualizar.form.submit()
        self.assertRedirects(resultado, reverse('pessoas-visualizar', args=[pessoa.pk,]))
        self.assertEqual('novo nome', Pessoa.objects.get(pk=pessoa.pk).nome)

