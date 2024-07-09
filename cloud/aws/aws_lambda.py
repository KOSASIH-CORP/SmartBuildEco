import boto3

lambda_client = boto3.client('lambda')

def invoke_lambda(function_name, payload):
    response = lambda_client.invoke(
        FunctionName=function_name,
        Payload=payload
    )
    return response
