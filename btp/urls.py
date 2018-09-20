"""btp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from main import views as main_views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', main_views.index, name='index'),
    url(r'^home/(?P<tab_id>[1-3]+)$', main_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login_page'),
    url(r'^logout/$', auth_views.logout, {'next_page':'login_page'}, name= 'logout_page'),
    url(r'^read/(?P<grievance_id>[0-9]+)/$', main_views.read, name='read'),
    url(r'^update/(?P<grievance_id>[0-9]+)/$', main_views.update, name='update_categories'),
    url(r'^add/$', main_views.add_grievance, name='add_grievance'),
    url(r'^resolve/(?P<grievance_id>[0-9]+)/$', main_views.resolve, name='resolve')
]