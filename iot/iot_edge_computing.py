import edgeiq

class IOTEdgeComputing:
    def __init__(self):
        self.device = edgeiq.Device()

    def deploy_model(self, model_path):
        self.device.deploy_model(model_path)

    def process_video(self, video_path):
        results = self.device.process_video(video_path)
        return results

    def process_image(self, image_path):
        results = self.device.process_image(image_path)
        return results

# Example usage:
iot_ec = IOTEdgeComputing()
model_path = 'model.tflite'
iot_ec.deploy_model(model_path)
video_path = 'video.mp4'
results = iot_ec.process_video(video_path)
print(results)
image_path = 'image.jpg'
results = iot_ec.process_image(image_path)
print(results)
