import os
import json
import boto3

class AWSLambdaFunction:
    def __init__(self, function_name, handler, runtime):
        self.function_name = function_name
        self.handler = handler
        self.runtime = runtime
        self.lambda_client = boto3.client('lambda')

    def create(self):
        # Create an AWS Lambda function
        response = self.lambda_client.create_function(
            FunctionName=self.function_name,
            Runtime=self.runtime,
            Role='arn:aws:iam::123456789012:role/lambda-execution-role',
            Handler=self.handler,
            Code={'ZipFile': bytes('def lambda_handler(event, context):\n    return {\n        "statusCode": 200,\n        "statusMessage": "OK"\n    }', 'utf-8')}
        )
        return response

    def invoke(self, event):
        # Invoke an AWS Lambda function
        response = self.lambda_client.invoke(
            FunctionName=self.function_name,
            InvocationType='RequestResponse',
            Payload=json.dumps(event)
        )
        return response

# Example usage
function_name = "my-lambda-function"
handler = "index.lambda_handler"
runtime = "python3.8"

aws_lambda_function = AWSLambdaFunction(function_name, handler, runtime)
aws_lambda_function.create()

event = {"key": "value"}
response = aws_lambda_function.invoke(event)
print(response)
