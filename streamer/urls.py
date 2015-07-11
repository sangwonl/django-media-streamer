from django.conf.urls import url


urlpatterns = [
    url(r'(?P<stream_path>.*)/$', 'streamer.views.get_stream'),
]
