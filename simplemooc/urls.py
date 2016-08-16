from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from rest_framework_jwt.views import obtain_jwt_token

from core import views


handler500 = views.handler500


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^contact/$', views.contact, name='contact'),
	url(
		r'^login/$', auth_views.login, {'template_name': 'login.html'},
		name='login'
	),
	url(r'^logout/$', auth_views.logout, {'next_page': 'index'}, name='logout'),
	url(r'^accounts/', include('accounts.urls', namespace='accounts')),
	url(r'^', include('courses.urls', namespace='courses')),
    url(r'^admin/', admin.site.urls),
	url(r'^api/cursos/', include('courses.api_urls', namespace='api_courses')),
	url(r'^api-token-auth/$', obtain_jwt_token),
]
