import os
import json
from azure.functions import FuncApp

class AzureFunction:
    def __init__(self, function_name, handler):
        self.function_name = function_name
        self.handler = handler
        self.func_app = FuncApp()

    def create(self):
        # Create an Azure Function
        self.func_app.create_function(
            self.function_name,
            self.handler,
            'python',
            '3.8'
        )

    def invoke(self, event):
        # Invoke an Azure Function
        response = self.func_app.invoke_function(
            self.function_name,
            event
        )
        return response

# Example usage
function_name = "my-azure-function"
handler = "main"

azure_function = AzureFunction(function_name, handler)
azure_function.create()

event = {"key": "value"}
response = azure_function.invoke(event)
print(response)
