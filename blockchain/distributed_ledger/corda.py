import os
import json
from corda_sdk_py import CordaSDK

class Corda:
    def __init__(self, network_config):
        self.sdk = CordaSDK(network_config)

    def deploy_cor_dapp(self, cor_dapp_path):
        # Deploy CorDapp to the network
        self.sdk.deploy_cor_dapp(cor_dapp_path)

    def start_flow(self, flow_class, flow_args):
        # Start a flow with arguments
        self.sdk.start_flow(flow_class, flow_args)

    def query_state(self, state_ref):
        # Query a state by reference
        self.sdk.query_state(state_ref)

# Example usage
network_config = {
    "name": "my_network",
    "node": "node.example.com"
}

corda = Corda(network_config)

cor_dapp_path = "path/to/cor_dapp"
corda.deploy_cor_dapp(cor_dapp_path)

flow_class = "com.example.MyFlow"
flow_args = ["arg1", "arg2"]
corda.start_flow(flow_class, flow_args)

state_ref = "state_ref_123"
result = corda.query_state(state_ref)
print(result)
