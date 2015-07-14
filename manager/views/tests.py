from django.template import loader
from django.template import RequestContext

from django.http import HttpResponse
from utils.networks import get_host_ip


HOST_IP = get_host_ip()


def simple_stream(req):
    t = loader.get_template('tests/simple_player.html')
    c = RequestContext(req, {'media_url': 'http://%s:8000/streamer/53c426c98cdf4ad8ac769177578418ce.mp4' % HOST_IP})
    return HttpResponse(t.render(c))


def dash_stream(req):
    t = loader.get_template('tests/dash_player.html')
    c = RequestContext(req, {'media_url': 'http://%s:8000/streamer/b520bc595ce04d708123abcca6fdbf5e.mpd' % HOST_IP})
    return HttpResponse(t.render(c))


def hls_stream(req):
    t = loader.get_template('tests/hls_player.html')
    c = RequestContext(req, {'media_url': 'http://%s:8000/streamer/ab1291c3fd9043dab94a3b9ffdfd5aad.m3u8' % HOST_IP})
    return HttpResponse(t.render(c))