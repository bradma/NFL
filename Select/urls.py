from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^(?P<user_id>\d+)/(?P<week_id>\d+)/$',
        views.select_game_week_one, name='week_one'),
    url(r'^(?P<user_id>\d+)/(?P<week_id>\d+)/weekSubmit/$',
        views.success_submit, name='submit'),
)
