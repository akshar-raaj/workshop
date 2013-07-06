from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'poll.views.index'),
    url(r'^(?P<poll_id>\d+)/$', 'poll.views.detail'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'poll.views.vote', name='vote_on_poll'),
    url(r'^(?P<poll_id>\d+)/result/$', 'poll.views.result', name='result_of_polls'),
)
