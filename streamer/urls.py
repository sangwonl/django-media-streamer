from django.conf.urls import url

urlpatterns = [
    url(r'test/', 'streamer.views.test_handler'),
]