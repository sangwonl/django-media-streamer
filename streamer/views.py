from django.http import HttpResponse

import json


def test_handler(req):
    test_content = json.dumps({'status': 0})
    return HttpResponse(content=test_content, status=200, content_type='application/json')