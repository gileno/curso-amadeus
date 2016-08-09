from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

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
]
