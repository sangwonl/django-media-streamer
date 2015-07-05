from django.views.static import serve
from main.settings import base

import os
import re


def get_stream(req, stream_name):
    req.META.pop('HTTP_IF_MODIFIED_SINCE', None)
    stream_token = re.split(r'[\._]+', stream_name)[0]
    media_root = os.path.join(base.MEDIA_ROOT, stream_token)
    return serve(request=req, path=stream_name, document_root=media_root, show_indexes=True)
