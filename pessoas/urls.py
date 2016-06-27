from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Listar.as_view(), name='pessoas-listar'),
    url(r'^adicionar/$', views.Adicionar.as_view(), name='pessoas-adicionar'),
    url(r'^(?P<pk>\d+)/$', views.Visualizar.as_view(), name='pessoas-visualizar'),
    url(r'^(?P<pk>\d+)/atualizar/$', views.Atualizar.as_view(), name='pessoas-atualizar'),
]
