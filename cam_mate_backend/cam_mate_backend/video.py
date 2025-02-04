import cv2

RTSP_URL = "rtsp://admin:Dead_6533@192.168.1.64:554/Streaming/Channels/101"

cap = cv2.VideoCapture(RTSP_URL)

if not cap.isOpened():
    print("Error: Cannot open RTSP stream")
else:
    print("RTSP stream opened successfully")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to read frame from stream")
            break

        cv2.imshow("RTSP Stream", frame)

        # Press 'q' to exit the stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()