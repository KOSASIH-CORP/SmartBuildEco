import os
import json
from azure.storage.blob import BlobServiceClient

class AzureIntegration:
    def __init__(self, azure_storage_account, azure_storage_access_key):
        self.azure_storage_account = azure_storage_account
        self.azure_storage_access_key = azure_storage_access_key
        self.blob_service_client = BlobServiceClient.from_connection_string(
            f"DefaultEndpointsProtocol=https;AccountName={azure_storage_account};AccountKey={azure_storage_access_key};BlobEndpoint=https://{azure_storage_account}.blob.core.windows.net/"
        )

    def upload_file(self, file_path, container_name):
        # Upload a file to Azure Blob Storage
        blob_client = self.blob_service_client.get_blob_client(container_name, os.path.basename(file_path))
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

    def create_function_app(self, function_app_name, handler):
        # Create an Azure Function App
        from azure.functions import FunctionApp
        function_app = FunctionApp(function_app_name, handler, 'python', '3.8')
        function_app.create()

# Example usage
azure_storage_account = "YOUR_AZURE_STORAGE_ACCOUNT"
azure_storage_access_key = "YOUR_AZURE_STORAGE_ACCESS_KEY"

azure_integration = AzureIntegration(azure_storage_account, azure_storage_access_key)
azure_integration.upload_file("path/to/file.txt", "my-container")
azure_integration.create_function_app("my-function-app", "main")
