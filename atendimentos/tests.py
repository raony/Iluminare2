from django.test import TestCase

from django_webtest import WebTest
from django.core.urlresolvers import reverse
from datetime import datetime

from pessoas.models import Pessoa
from salas.models import Sala
from tratamento.models import Tratamento, Sessao
from .models import Atendimento

# unit

class AtendimentoEntradaTeste(WebTest):
    def test_busca(self):
        self.fail("falta implementar")