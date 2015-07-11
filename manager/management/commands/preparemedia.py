import os
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

import uuid
import commands


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--stream_type', type=str)
        parser.add_argument('--input_file', type=str)
        parser.add_argument('--output_dir', type=str)

    def handle(self, *args, **options):
        stream_type = options['stream_type']
        input_file = options['input_file']
        output_dir = options['output_dir']

        if not all([stream_type, input_file, output_dir]):
            raise CommandError('Invalid parameters.')

        stream_type_handlers = {'dash': self.handle_dash, 'hls': self.handle_hls}
        if stream_type not in stream_type_handlers.keys():
            raise CommandError('Streaming type must be dash or hls.')

        hash_name = str(uuid.uuid4().hex)
        media_cache_dir = os.path.join(output_dir, hash_name)
        if not os.path.exists(media_cache_dir): os.makedirs(media_cache_dir)

        handler = stream_type_handlers[stream_type]
        handler(input_file, media_cache_dir, hash_name)

    def handle_dash(self, input_file, cache_dir, hash_name):
        pass

    def handle_hls(self, input_file, cache_dir, hash_name):
        profile_opts = '-profile:v high -level:v 4.1'
        codec_options = '-codec:v libx264 -codec:a libfaac'
        m3u8_path = os.path.join(cache_dir, '%s.m3u8' % hash_name)
        ts_path = os.path.join(cache_dir, '%s_%s.ts' % (hash_name, '%06d'))

        ffmpeg_cmd = 'ffmpeg -i %s -map 0 %s %s -f ssegment -segment_list %s -segment_list_flags +live ' \
                     '-segment_time 4 %s' % (input_file, profile_opts, codec_options, m3u8_path, ts_path)

        self.stdout.write(ffmpeg_cmd)
        commands.getoutput(ffmpeg_cmd)

