from django.conf.urls import url


urlpatterns = [
    url(r'test_dash/$', 'manager.views.test_dash'),
    url(r'test_hls/$', 'manager.views.test_hls'),
]