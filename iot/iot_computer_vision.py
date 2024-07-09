import cv2
import numpy as np

class IOTComputerVision:
    def __init__(self):
        self.net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

    def detect_objects(self, image):
        blob =cv2.dnn.blobFromImage(image, 1/255, (416, 416), [0,0,0], 1, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.getOutputsNames(self.net))
        return outs

    def getOutputsNames(self, net):
        layersNames = net.getLayerNames()
        return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    def draw_bounding_boxes(self, image, outs):
        for out in outs:
            for detection in out:
                scores = detection[5:]
                classId = np.argmax(scores)
                confidence = scores[classId]
                if confidence > 0.5 and classId == 0:
                    x, y, w, h = detection[0:4] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
                    cv2.rectangle(image, (int(x), int(y)), (int(x+w), int(y+h)), (255, 0, 0), 2)
                    cv2.putText(image, f'Person: {confidence:.2f}', (int(x), int(y-10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        return image

# Example usage:
iot_cv = IOTComputerVision()
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    outs = iot_cv.detect_objects(frame)
    frame = iot_cv.draw_bounding_boxes(frame, outs)
    cv2.imshow('Object Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
