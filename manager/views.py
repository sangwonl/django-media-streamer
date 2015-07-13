from django.template import loader
from django.template import RequestContext

from django.http import HttpResponse
from common.utils import get_ip_addr


def test_simple(req):
    t = loader.get_template('simple_player.html')
    c = RequestContext(req, {
        'media_url': 'http://%s:8000/streamer/53c426c98cdf4ad8ac769177578418ce.mp4/' % get_ip_addr()
    })
    return HttpResponse(t.render(c))


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


def cast_receiver(req):
    t = loader.get_template('cast_receiver.html')
    c = RequestContext(req, {})

    res = HttpResponse(t.render(c))
    res['Access-Control-Allow-Origin'] = '*'
    res['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE'
    res['Access-Control-Allow-Headers'] = 'Content-Type'
    return res