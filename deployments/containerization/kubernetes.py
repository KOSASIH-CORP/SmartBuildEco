import os
import json
from kubernetes import client, config

class KubernetesDeployment:
    def __init__(self, deployment_config):
        self.deployment_config = deployment_config
        self.kube_config = config.load_kube_config()

    def deploy(self):
        # Create a Kubernetes deployment
        api = client.AppsV1Api()
        deployment = client.V1Deployment()
        deployment.metadata = client.V1ObjectMeta(name="my-deployment")
        deployment.spec = client.V1DeploymentSpec(
            replicas=3,
            selector=client.V1LabelSelector(match_labels={"app": "my-app"}),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "my-app"}),
                spec=client.V1PodSpec(containers=[
                    client.V1Container(
                        name="my-app",
                        image="my-image:latest",
                        ports=[client.V1ContainerPort(container_port=80)]
                    )
                ])
            )
        )
        api.create_namespaced_deployment(namespace="default", body=deployment)

    def undeploy(self):
        # Delete a Kubernetes deployment
        api = client.AppsV1Api()
        api.delete_namespaced_deployment(name="my-deployment", namespace="default")

# Example usage
deployment_config = {
    "image": "my-image:latest",
    "replicas": 3
}

kubernetes_deployment = KubernetesDeployment(deployment_config)
kubernetes_deployment.deploy()
