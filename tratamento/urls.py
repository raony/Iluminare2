from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tratamento/$', views.ListarTratamento.as_view(), name='tratamento-listar'),
    url(r'^tratamento/adicionar/$', views.AdicionarTratamento.as_view(), name='tratamento-adicionar'),
    url(r'^tratamento/(?P<pk>\d+)/$', views.VisualizarTratamento.as_view(), name='tratamento-visualizar'),
    url(r'^tratamento/(?P<pk>\d+)/atualizar/$', views.AtualizarTratamento.as_view(), name='tratamento-atualizar'),

    url(r'^pessoas/(?P<pk>\d+)/tratamento/$', views.ListarTratamento.as_view(), name='tratamento-pessoa-listar'),
    url(r'^pessoas/(?P<pk>\d+)/tratamento/adicionar/$', views.AdicionarTratamento.as_view(), name='tratamento-pessoa-adicionar'),
]
