#!/bin/bash

rm videos.txt || true
for i in *.mp4
do
ffmpeg -y -r:v "480/1" -i "$i" -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2,setsar=1,format=yuv420p"  -b:v 4M -an -vcodec vp9 -r:v "60/1" "$i.enc.mkv"
echo file \'"./$i.enc.mkv"\' >> videos.txt
done

ffmpeg -y -f concat -safe 0 -i videos.txt -c copy $1.mkv
rm *.mp4 *.enc.mkv
