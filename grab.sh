scp pi@192.168.1.142:~/recordings/*.h264 /mnt/e/scratch/picam/raw
for f in /mnt/e/scratch/picam/raw/*.h264; do MP4Box -add "$f" "$f.mp4";done
mv /mnt/e/scratch/picam/raw/*.h264 /mnt/e/scratch/picam/rawdone
mv /mnt/e/scratch/picam/raw/*.mp4 /mnt/e/scratch/picam/mp4
