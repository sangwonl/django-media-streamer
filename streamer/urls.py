from django.conf.urls import url


urlpatterns = [
    url(r'(?P<stream_name>.*)/$', 'streamer.views.get_stream'),
]
