import os
import json
from google.cloud import functions_v2

class GoogleCloudFunction:
    def __init__(self, function_name, handler):
        self.function_name = function_name
        self.handler = handler
        self.client = functions_v2.CloudFunctionsClient()

    def create(self):
        # Create a Google Cloud Function
        region = "us-central1"
        service = "my-service"
        self.client.create_function(
            parent=f"projects/{os.environ.get('GOOGLE_CLOUD_PROJECT')}/locations/{region}",
            function=self.function_name,
            function_spec=self.client.function_spec.FunctionSpec(
                runtime="python3.8",
                entry_point=self.handler,
                source_archive_url="gs://my-bucket/my-function.zip"
            ),
            service=service
        )

    def invoke(self, event):
        # Invoke a Google Cloud Function
        response = self.client.call(
            function_name=self.function_name,
            service=self.function_name,
            request={
                "data": event
            }
        )
        return response

# Example usage
function_name = "my-google-cloud-function"
handler = "main"

google_cloud_function = GoogleCloudFunction(function_name, handler)
google_cloud_function.create()

event = {"key": "value"}
response = google_cloud_function.invoke(event)
print(response)
