import cv2
import os
from datetime import datetime

def detect_motion(video_path, gap=5, min_area=500):
    # Extract video name without extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Create timestamp string
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Output folder: motion_frames/video1_20250805_181045/
    folder_name = f"{video_name}_{timestamp}"
    output_dir = os.path.join("motion_frames", folder_name)
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frames = []
    fcount = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(gray)
        if len(frames) > gap + 1:
            frames.pop(0)

        cv2.putText(frame, f"Frame Count: {fcount}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if len(frames) > gap:
            diff = cv2.absdiff(frames[0], frames[-1])
            _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
            contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            motion = False
            for c in contours:
                if cv2.contourArea(c) < min_area:
                    continue
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                motion = True

            if motion:
                cv2.putText(frame, "Motion Detected", (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                frame_name = f"frame_{fcount}.jpg"
                frame_path = os.path.join(output_dir, frame_name)
                cv2.imwrite(frame_path, frame)
                print(f"📸 Saved: {frame_path}")

        cv2.imshow("Motion Detection", frame)
        fcount += 1

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Run for one or more videos
video_list = ["video_ex.mp4"]

for video in video_list:
    detect_motion(video)
