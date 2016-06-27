from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ListarSala.as_view(), name='salas-listar'),
    url(r'^adicionar/$', views.AdicionarSala.as_view(), name='salas-adicionar'),
    url(r'^(?P<pk>\d+)/$', views.VisualizarSala.as_view(), name='salas-visualizar'),
    url(r'^(?P<pk>\d+)/atualizar/$', views.AtualizarSala.as_view(), name='salas-atualizar'),
]
