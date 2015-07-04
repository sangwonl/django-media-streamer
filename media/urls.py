from django.conf.urls import url

urlpatterns = [
    url(r'test/', 'media.views.test_handler'),
]