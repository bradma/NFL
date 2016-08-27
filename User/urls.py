from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns('',
    url(r'^(?P<user_id>\d+)/$', views.main_user, name='user_core'),
    url(r'^WeekView/', include('Select.urls', namespace='week_one')),
    url(r'^(?P<user_id>\d+)/(?P<week_id>\d+)/detailview/$', views.week_detail.as_view(), name='detailView'),
    url(r'(?P<user_id>\d+)/TeamName/$', views.user_team, name='teamname'),
)
