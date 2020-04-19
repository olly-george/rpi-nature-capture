scp pi@192.168.1.140:~/recordings/*.h264 /mnt/d/scratch/picam/raw
for f in /mnt/d/scratch/picam/raw/*.h264; do MP4Box -add "$f" "$f.mp4";done
mv /mnt/d/scratch/picam/raw/*.h264 /mnt/d/scratch/picam/rawdone
mv /mnt/d/scratch/picam/raw/*.mp4 /mnt/d/scratch/picam/mp4
