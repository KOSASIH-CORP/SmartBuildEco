import os
import json
from fabric_sdk_py import FabricSDK

class HyperledgerFabric:
    def __init__(self, network_config):
        self.sdk = FabricSDK(network_config)

    def deploy_chaincode(self, chaincode_path, chaincode_id, chaincode_version):
        # Deploy chaincode to the network
        self.sdk.deploy_chaincode(chaincode_path, chaincode_id, chaincode_version)

    def invoke_chaincode(self, chaincode_id, chaincode_version, func, args):
        # Invoke chaincode function with arguments
        self.sdk.invoke_chaincode(chaincode_id, chaincode_version, func, args)

    def query_chaincode(self, chaincode_id, chaincode_version, func, args):
        # Query chaincode function with arguments
        self.sdk.query_chaincode(chaincode_id, chaincode_version, func, args)

# Example usage
network_config = {
    "name": "my_network",
    "orderer": "orderer.example.com",
    "peers": ["peer0.example.com", "peer1.example.com"]
}

hyperledger_fabric = HyperledgerFabric(network_config)

chaincode_path = "path/to/chaincode"
chaincode_id = "my_chaincode"
chaincode_version = "1.0"

hyperledger_fabric.deploy_chaincode(chaincode_path, chaincode_id, chaincode_version)

func = "init"
args = ["arg1", "arg2"]
hyperledger_fabric.invoke_chaincode(chaincode_id, chaincode_version, func, args)

func = "query"
args = ["arg1"]
result = hyperledger_fabric.query_chaincode(chaincode_id, chaincode_version, func, args)
print(result)
