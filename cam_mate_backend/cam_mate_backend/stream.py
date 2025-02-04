from flask import Flask, Response
from flask_cors import CORS
import cv2

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Allow cross-origin WebSocket connections

# Your RTSP stream URL
RTSP_URL = "rtsp://admin:Dead_6533@192.168.1.64:554/Streaming/Channels/101"

def generate_frames():
    cap = cv2.VideoCapture(RTSP_URL)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
