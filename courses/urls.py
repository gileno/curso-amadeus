from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cursos/$', views.IndexView.as_view(), name='index'),
    url(r'^cursos/([\w_-]+)/$', views.course, name='course'),
    url(r'^categorias/([\w_-]+)/$', views.category, name='category'),
]
