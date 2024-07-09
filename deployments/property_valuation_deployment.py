import os
import json
from kubernetes import client, config

class PropertyValuationDeployment:
    def __init__(self, deployment_config):
        self.deployment_config = deployment_config
        self.kube_config = config.load_kube_config()

    def deploy(self):
        # Create a Kubernetes deployment
        api = client.AppsV1Api()
        deployment = client.V1Deployment()
        deployment.metadata = client.V1ObjectMeta(name="property-valuation")
        deployment.spec = client.V1DeploymentSpec(
            replicas=3,
            selector=client.V1LabelSelector(match_labels={"app": "property-valuation"}),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "property-valuation"}),
                spec=client.V1PodSpec(containers=[
                    client.V1Container(
                        name="property-valuation",
                        image="property-valuation:latest",
                        ports=[client.V1ContainerPort(container_port=80)]
                    )
                ])
            )
        )
        api.create_namespaced_deployment(namespace="default", body=deployment)

    def undeploy(self):
        # Delete a Kubernetes deployment
        api = client.AppsV1Api()
        api.delete_namespaced_deployment(name="property-valuation", namespace="default")

# Example usage
deployment_config = {
    "image": "property-valuation:latest",
    "replicas": 3
}

property_valuation_deployment = PropertyValuationDeployment(deployment_config)
property_valuation_deployment.deploy()
