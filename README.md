## Generate Variable Bitrates
```
$ ffmpeg -i <inputfile>.mp4 -r 30 -g 30 -profile:v high -level:v 4.1 -c:a libfdk_aac -c:v libx264 -b:v 3000k -maxrate 5000k -bufsize 15k -vf "scale=1280:-1" <outputfile>_3000k.mp4

$ ffmpeg -i <inputfile>.mp4 -r 30 -g 30 -profile:v high -level:v 4.1 -c:a libfdk_aac -c:v libx264 -b:v 2000k -maxrate 3000k -bufsize 10k -vf "scale=1280:-1" <outputfile>_2000k.mp4

$ ffmpeg -i <inputfile>.mp4 -r 30 -g 30 -profile:v high -level:v 4.1 -c:a libfdk_aac -c:v libx264 -b:v 1000k -maxrate 2000k -bufsize 8k -vf "scale=1280:-1" <outputfile>_1000k.mp4
```

## Generate Segments
```
$ MP4Box -dash 2000 -rap -frag-rap -profile live -out <outputfile> <inputfile1>.mp4 <inputfile2>.mp4 <inputfile3>.mp4
```