from django.conf.urls import url


urlpatterns = [
    url(r'test_page/$', 'manager.views.test_page'),
]