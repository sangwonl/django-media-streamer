# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cache_hash_name', models.CharField(max_length=255)),
                ('media_title', models.CharField(max_length=255)),
                ('media_type', models.CharField(max_length=4, choices=[(b'VID', b'video'), (b'AUD', b'audio')])),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_src_dir', models.CharField(max_length=255)),
                ('media_cache_dir', models.CharField(max_length=255)),
            ],
        ),
    ]
