import os
import json
from google.cloud import storage

class GoogleCloudIntegration:
    def __init__(self, google_cloud_project_id, google_cloud_storage_bucket_name):
        self.google_cloud_project_id = google_cloud_project_id
        self.google_cloud_storage_bucket_name = google_cloud_storage_bucket_name
        self.storage_client = storage.Client()

    def upload_file(self, file_path):
        # Upload a file to Google Cloud Storage
        bucket = self.storage_client.bucket(self.google_cloud_storage_bucket_name)
        blob = bucket.blob(os.path.basename(file_path))
        blob.upload_from_filename(file_path)

    def create_cloud_function(self, function_name, handler):
        # Create a Google Cloud Function
        from google.cloud import functions_v2
        client = functions_v2.CloudFunctionsServiceClient()
        parent = f"projects/{self.google_cloud_project_id}/locations/us-central1"
        function = client.create_function(
            parent=parent,
            function=function_name,
            function_spec=functions_v2.FunctionSpec(
                runtime="python3.8",
                entry_point=handler,
                source_archive_url=f"gs://{self.google_cloud_storage_bucket_name}/{os.path.basename(file_path)}"
            )
        )

# Example usage
google_cloud_project_id = "YOUR_GOOGLE_CLOUD_PROJECT_ID"
google_cloud_storage_bucket_name = "YOUR_GOOGLE_CLOUD_STORAGE_BUCKET_NAME"

google_cloud_integration = GoogleCloudIntegration(google_cloud_project_id, google_cloud_storage_bucket_name)
google_cloud_integration.upload_file("path/to/file.txt")
google_cloud_integration.create_cloud_function("my-cloud-function", "main")
