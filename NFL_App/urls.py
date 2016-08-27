from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns('',
#Login Panel
    url(r'^$', views.login_site , name='login'),
#User Main
    url(r'^User/', include('User.urls', namespace='user_main')),
#Admin Console
    url(r'^admin/', include(admin.site.urls)),
#Logout
    url(r'^logout/$', views.logout_view, name='logout'),
#Test
    url(r'^test/$', TemplateView.as_view(template_name='test.html')),
)
