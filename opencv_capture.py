import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;tcp"
import cv2
import time

# Replace this with your RTSP URL
rtsp_url = "rtsp://localhost:8554/mystream?tcp"
cap = cv2.VideoCapture(rtsp_url, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print("❌ Cannot open RTSP stream")
    exit()

print("✅ Connected to RTSP stream")

frame_count = 0
max_frames = 5  # Stop after 5 frames
interval = 5  # seconds
start_time = time.time()

while frame_count < max_frames:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Failed to read frame (stream ended or connection lost)")
        break

    current_time = time.time()
    if current_time - start_time >= interval:
        frame_count += 1
        filename = f"frame_{frame_count:03d}.jpg"
        cv2.imwrite(filename, frame)
        print(f"🖼️  Saved {filename}")
        start_time = current_time

cap.release()
print("✅ Finished capturing frames")
