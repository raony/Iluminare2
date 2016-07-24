from django.test import TestCase
from django.utils import timezone

now = timezone.now()
from django_webtest import WebTest
from django.core.urlresolvers import reverse
from datetime import datetime

from pessoas.models import Pessoa
from salas.models import Sala
from tratamento.models import Tratamento, Sessao
from .models import Atendimento

# funcional

class AtendimentoEntradaTeste(WebTest):
    def test_busca_vazia(self):
        pessoa1 = Pessoa.objects.create(nome='antônio', sobrenome=' Pessoa ')
        pessoa2 = Pessoa.objects.create(nome='antobaldo luís', sobrenome=' silva filho ')
        pessoa3 = Pessoa.objects.create(nome='luiz', sobrenome='pessoa silva')

        atendimento_entrada = self.app.get(reverse('atendimentos-entrada'))

        self.assertNotContains(atendimento_entrada, 'Antônio')
        self.assertNotContains(atendimento_entrada, 'Antobaldo')
        self.assertNotContains(atendimento_entrada, 'Luiz')

    def test_busca(self):
        pessoa1 = Pessoa.objects.create(nome='antônio', sobrenome=' Pessoa ')
        pessoa2 = Pessoa.objects.create(nome='antobaldo luís', sobrenome=' silva filho ')
        pessoa3 = Pessoa.objects.create(nome='luiz', sobrenome='pessoa silva')

        atendimento_entrada = self.app.get(reverse('atendimentos-entrada'))

        atendimento_entrada.form['q'] = 'ant'
        resultado = atendimento_entrada.form.submit()

        self.assertEquals(reverse('atendimentos-entrada'), resultado.request.path)
        self.assertContains(resultado, 'Antônio')
        self.assertContains(resultado, 'Antobaldo')
        self.assertNotContains(resultado, 'Luiz')

        self.assertEquals('ant', resultado.form['q'].value)

class AtendimentoVisualizarTeste(WebTest):
    def test_nao_mostra_atendimentos_passados(self):
        pessoa1 = Pessoa.objects.create(nome='antônio', sobrenome=' Pessoa ')

        now = timezone.now()

        atendimento = Atendimento.objects.create(paciente=pessoa1, evento=Atendimento.EVENTOS[0][0])
        atendimento2 = Atendimento.objects.create(hora=timezone.make_aware(datetime(now.year-1, now.month, now.day)),
                                                    paciente=pessoa1,
                                                    evento=Atendimento.EVENTOS[1][0])

        resultado = self.app.get(reverse('atendimentos-visualizar', args=(pessoa1.pk,)))
        self.assertContains(resultado, Atendimento.EVENTOS[0][1])
        self.assertNotContains(resultado, Atendimento.EVENTOS[1][1])

