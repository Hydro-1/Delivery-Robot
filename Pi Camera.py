### Setting Up the Pi Camera and OpenCV ###

import cv2

cap = cv2.VideoCapture(0)

# Begin execution
while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('frame', frame)

    # Stop execution
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()