# Simple docker compose for mocking rtsp stream from video

##
- run dokcer compose
```
docker compose up -d
```

- test rtsp link
```
rtsp://localhost:8554/mystream
```

- test cli
```
ffmpeg -rtsp_transport tcp -i rtsp://localhost:8554/mystream -c copy out.mp4
```
