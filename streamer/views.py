from django.views.static import serve
from main.settings import base

import os
import re


def get_stream(req, stream_name):
    # stream_name could be '<media_token>.mpd' or '<media_token>_<bitrate>_<idx>.m4s'
    stream_token = re.split(r'[\._]+', stream_name)[0]
    media_root = os.path.join(base.MEDIA_ROOT, stream_token)
    return serve(request=req, path=stream_name, document_root=media_root, show_indexes=True)
