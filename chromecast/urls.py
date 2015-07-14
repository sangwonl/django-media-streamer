from django.conf.urls import url


urlpatterns = [
    url(r'receiver/$', 'chromecast.views.simple_player'),
]