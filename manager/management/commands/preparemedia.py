from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

import os
import uuid
import commands


FFMPEG_FPS_OPTS = '-r 30 -g 30'
FFMPEG_PROFILE_OPTS = '-profile:v high -level:v 4.1'
FFMPEG_CODEC_OPTS = '-codec:v libx264 -codec:a libfaac'


class Command(BaseCommand):
    stream_type = ''
    input_file = ''
    output_dir = ''

    def add_arguments(self, parser):
        parser.add_argument('--stream-type', type=str)
        parser.add_argument('--input-file', type=str)
        parser.add_argument('--output-dir', type=str)

    def handle(self, *args, **options):
        self._parse_params(options)
        stream_type_handlers = {
            'simple': self.handle_simple,
            'dash': self.handle_dash,
            'hls': self.handle_hls
        }
        if self.stream_type not in stream_type_handlers.keys():
            raise CommandError('Streaming type must be dash or hls.')

        hash_name = str(uuid.uuid4().hex)
        cache_dir = self._create_cache_dir(hash_name)
        stream_type_handlers[self.stream_type](cache_dir, hash_name)

    # Stream handlers
    def handle_simple(self, cache_dir, hash_name):
        output_dir = os.path.join(cache_dir, '%s.mp4' % hash_name)

        self._ffmpeg_transcode(output_dir)

    def handle_dash(self, cache_dir, hash_name):
        temp_dir = self._create_temp_dir(hash_name)
        temp_path = os.path.join(temp_dir, '%s.mp4' % hash_name)

        self._ffmpeg_transcode(temp_path)

        self._mp4box_dash_segmentation(cache_dir, temp_path, hash_name)

    def handle_hls(self, cache_dir, hash_name):
        m3u8_path = os.path.join(cache_dir, '%s.m3u8' % hash_name)
        ts_path = os.path.join(cache_dir, '%s_%s.ts' % (hash_name, '%06d'))

        self._ffmpeg_transcode_and_hls_segmentation(m3u8_path, ts_path)

    # Common methods
    def _parse_params(self, opts):
        params = (opts['stream_type'], opts['input_file'], opts['output_dir'])
        if not all(params):
            raise CommandError('Invalid parameters.')

        self.stream_type, self.input_file, self.output_dir = params

    @staticmethod
    def _create_dir(path):
        if not os.path.exists(path):
            os.makedirs(path)

    def _create_cache_dir(self, hash_name):
        media_cache_dir = os.path.join(self.output_dir, hash_name)
        self._create_dir(media_cache_dir)
        return media_cache_dir

    def _create_temp_dir(self, hash_name):
        media_temp_dir = os.path.join(self.output_dir, '../temp/%s' % hash_name)
        self._create_dir(media_temp_dir)
        return media_temp_dir

    def _ffmpeg_transcode(self, output_path):
        ffmpeg_cmd = 'ffmpeg -i %s %s %s %s %s' % (
            self.input_file, FFMPEG_FPS_OPTS, FFMPEG_PROFILE_OPTS, FFMPEG_CODEC_OPTS, output_path)
        self.stdout.write(ffmpeg_cmd)
        commands.getoutput(ffmpeg_cmd)

    def _mp4box_dash_segmentation(self, cache_dir, temp_path, hash_name):
        output_path = os.path.join(cache_dir, hash_name)
        mp4box_cmd = 'MP4Box -dash 4000 -rap -frag-rap -profile live -url-template ' \
                     '-segment-name %s_ -out %s %s' % ('%s', output_path[2:], temp_path)
        self.stdout.write(mp4box_cmd)
        commands.getoutput(mp4box_cmd)

    def _ffmpeg_transcode_and_hls_segmentation(self, m3u8_path, ts_path):
        ffmpeg_cmd = 'ffmpeg -i %s -map 0 %s %s -f ssegment -segment_list %s -segment_list_flags +live ' \
                     '-segment_time 4 %s' % (self.input_file, FFMPEG_PROFILE_OPTS, FFMPEG_CODEC_OPTS, m3u8_path, ts_path)
        self.stdout.write(ffmpeg_cmd)
        commands.getoutput(ffmpeg_cmd)

