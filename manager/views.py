from django.template import loader
from django.template import RequestContext

from django.http import HttpResponse


def test_page(req):
    t = loader.get_template('dash_player.html')
    c = RequestContext(req, {})
    return HttpResponse(t.render(c))
