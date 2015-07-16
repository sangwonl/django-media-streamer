## Run server
```
$ pip install -r requirements/dev.txt
$ python manage.py runserver {MY_IP}:8000
```

## Play Test on Browser
HLS Streaming::
```
Connect to http://{MY_IP}:8000/manager/test_hls/
```

MPEG-DASH Streaming::
```
Connect to http://{MY_IP}:8000/manager/test_dash/
```

## Prepare Media for Streaming
1. Assume the media is placed at {Project Root}/library/video
2. At {Project Root}, issue 'python manage.py preparemedia'
HLS(m3u8/ts)::
```
python manage.py preparemedia --stream-type hls --input-file ./library/video/sample.mp4 --output-dir ./library/cache
```
MPEG-DASH(mpd/m4s)::
```
python manage.py preparemedia --stream-type dash --input-file ./library/video/sample.mp4 --output-dir ./library/cache
```

*Above commands will carry out transcoding and segmentation of input media, then save them into output directory with hash name.*
