from django.template import loader
from django.template import RequestContext

from django.http import HttpResponse


def simple_player(req):
    t = loader.get_template('receivers/simple_player.html')
    c = RequestContext(req, {})
    return HttpResponse(t.render(c))
