import os
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

import uuid
import commands


FFMPEG_FPS_OPTS = '-r 30 -g 30'
FFMPEG_PROFILE_OPTS = '-profile:v high -level:v 4.1'
FFMPEG_CODEC_OPTS = '-codec:v libx264 -codec:a libfaac'


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
        # Create temporary folder for transcoded media
        media_temp_dir = os.path.join(cache_dir, '../../temp/%s' % hash_name)
        if not os.path.exists(media_temp_dir): os.makedirs(media_temp_dir)
        temp_path = os.path.join(media_temp_dir, '%s.mp4' % hash_name)

        # Run ffmpeg command for transcoding
        ffmpeg_cmd = 'ffmpeg -i %s %s %s %s %s' % (
            input_file, FFMPEG_FPS_OPTS, FFMPEG_PROFILE_OPTS, FFMPEG_CODEC_OPTS, temp_path)
        self.stdout.write(ffmpeg_cmd)
        commands.getoutput(ffmpeg_cmd)

        # Run mp4box command for segmentation
        output_path = os.path.join(cache_dir, hash_name)
        mp4box_cmd = 'MP4Box -dash 2000 -rap -frag-rap -profile live -url-template ' \
                     '-segment-name %s_ -out %s %s' % ('%s', output_path[2:], temp_path)
        self.stdout.write(mp4box_cmd)
        commands.getoutput(mp4box_cmd)

    def handle_hls(self, input_file, cache_dir, hash_name):
        m3u8_path = os.path.join(cache_dir, '%s.m3u8' % hash_name)
        ts_path = os.path.join(cache_dir, '%s_%s.ts' % (hash_name, '%06d'))

        # Run ffmpeg command for transcoding and segmentation
        ffmpeg_cmd = 'ffmpeg -i %s -map 0 %s %s -f ssegment -segment_list %s -segment_list_flags +live ' \
                     '-segment_time 4 %s' % (input_file, FFMPEG_PROFILE_OPTS, FFMPEG_CODEC_OPTS, m3u8_path, ts_path)
        self.stdout.write(ffmpeg_cmd)
        commands.getoutput(ffmpeg_cmd)

