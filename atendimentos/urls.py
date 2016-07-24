from django.conf.urls import url
from . import views as atendimentos

urlpatterns = [
    url(r'^$', atendimentos.Entrada.as_view(), name='atendimentos-entrada'),
    url(r'^(?P<pk>\d+)/$', atendimentos.Visualizar.as_view(), name='atendimentos-visualizar'),
]
