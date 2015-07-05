from django.db import models


class Preference(models.Model):
    media_src_dir = models.CharField(max_length=255)
    media_cache_dir = models.CharField(max_length=255)


class Library(models.Model):
    MEDIA_TYPE_VIDEO = 'VID'
    MEDIA_TYPE_AUDIO = 'AUD'
    MEDIA_TYPES = (
        (MEDIA_TYPE_VIDEO, 'video'),
        (MEDIA_TYPE_AUDIO, 'audio')
    )

    cache_hash_name = models.CharField(max_length=255)
    media_title = models.CharField(max_length=255)
    media_type = models.CharField(max_length=4, choices=MEDIA_TYPES)
