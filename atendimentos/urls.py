from django.conf.urls import url
from . import views as atendimentos

urlpatterns = [
    url(r'^atendimentos/$', atendimentos.Entrada.as_view(), name='atendimentos-entrada'),
]
