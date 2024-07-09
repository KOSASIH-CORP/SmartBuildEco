import cv2
import numpy as np

class IOTAugmentedReality:
    def __init__(self):
        self.aruco_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)

    def detect_markers(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray, self.aruco_dict)
        return corners, ids

    def draw_augmented_reality(self, image, corners, ids):
        for corner, id in zip(corners, ids):
            x, y, w, h = cv2.boundingRect(corner)
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(image, f'ID: {id}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        return image

# Example usage:
iot_ar = IOTAugmentedReality()
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    corners, ids = iot_ar.detect_markers(frame)
    frame = iot_ar.draw_augmented_reality(frame, corners, ids)
    cv2.imshow('Augmented Reality', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
