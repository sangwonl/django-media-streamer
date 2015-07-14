from django.conf.urls import url


urlpatterns = [
    url(r'test_simple/$', 'manager.views.tests.simple_stream'),
    url(r'test_dash/$', 'manager.views.tests.dash_stream'),
    url(r'test_hls/$', 'manager.views.tests.hls_stream'),
]