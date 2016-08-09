# coding=utf-8
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^edit/$', views.edit_user, name='edit_user'),
    url(r'^registrar/$', views.RegisterView.as_view(), name='register'),
    url(r'^cursos/$', views.CoursesView.as_view(), name='student_courses'),
]
