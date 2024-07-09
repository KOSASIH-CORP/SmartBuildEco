import os
import json
import boto3

class AWSIntegration:
    def __init__(self, aws_access_key_id, aws_secret_access_key):
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.s3 = boto3.client('s3')

    def upload_file(self, file_path, bucket_name):
        # Upload a file to AWS S3
        self.s3.upload_file(file_path, bucket_name, os.path.basename(file_path))

    def create_lambda_function(self, function_name, handler):
        # Create an AWS Lambda function
        lambda_client = boto3.client('lambda')
        lambda_client.create_function(
            FunctionName=function_name,
            Runtime='python3.8',
            Role='arn:aws:iam::123456789012:role/lambda-execution-role',
            Handler=handler,
            Code={'ZipFile': bytes('def lambda_handler(event, context):\n    return {\n        "statusCode": 200,\n        "statusMessage": "OK"\n    }', 'utf-8')}
        )

# Example usage
aws_access_key_id = "YOUR_AWS_ACCESS_KEY_ID"
aws_secret_access_key = "YOUR_AWS_SECRET_ACCESS_KEY"

aws_integration = AWSIntegration(aws_access_key_id, aws_secret_access_key)
aws_integration.upload_file("path/to/file.txt", "my-bucket")
aws_integration.create_lambda_function("my-lambda-function", "index.lambda_handler")
