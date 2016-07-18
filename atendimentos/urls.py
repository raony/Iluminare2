from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tratamentos/$', views.ListarTratamento.as_view(), name='tratamentos-listar'),
    url(r'^tratamentos/adicionar/$', views.AdicionarTratamento.as_view(), name='tratamentos-adicionar'),
    url(r'^tratamentos/(?P<pk>\d+)/$', views.VisualizarTratamento.as_view(), name='tratamentos-visualizar'),
    url(r'^tratamentos/(?P<pk>\d+)/atualizar/$', views.AtualizarTratamento.as_view(), name='tratamentos-atualizar'),

    url(r'^pessoas/(?P<pk>\d+)/tratamentos/$', views.ListarTratamento.as_view(), name='tratamentos-pessoa-listar'),
    url(r'^pessoas/(?P<pessoapk>\d+)/tratamentos/adicionar/$', views.AdicionarTratamento.as_view(),
        name='tratamentos-pessoa-adicionar'),

    url(r'^tratamentos/(?P<tratamentopk>\d+)/sessoes/adicionar/$', views.AdicionarSessao.as_view(),
        name='sessoes-adicionar'),

    url(r'^tratamentos/(?P<tratamentopk>\d+)/sessoes/remover/(?P<pk>\d+)/$', views.RemoverSessao.as_view(),
        name='sessoes-remover'),
]
