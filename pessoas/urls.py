from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Listar.as_view(), name='pessoas-listar'),
]
