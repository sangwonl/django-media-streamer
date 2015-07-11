from django.template import loader
from django.template import RequestContext

from django.http import HttpResponse

import socket


def get_ip_addr():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return s.getsockname()[0]


def test_dash(req):
    t = loader.get_template('dash_player.html')
    c = RequestContext(req, {
        'media_url': 'http://%s:8000/streamer/b520bc595ce04d708123abcca6fdbf5e.mpd/' % get_ip_addr()
    })
    return HttpResponse(t.render(c))


def test_hls(req):
    t = loader.get_template('hls_player.html')
    c = RequestContext(req, {
        'media_url': 'http://%s:8000/streamer/ab1291c3fd9043dab94a3b9ffdfd5aad.m3u8/' % get_ip_addr()
    })
    return HttpResponse(t.render(c))
