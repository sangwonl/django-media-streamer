from django.conf.urls import url


urlpatterns = [
    url(r'test_simple/$', 'manager.views.test_simple'),
    url(r'test_dash/$', 'manager.views.test_dash'),
    url(r'test_hls/$', 'manager.views.test_hls'),

    url(r'cast/receiver/$', 'manager.views.cast_receiver'),
]