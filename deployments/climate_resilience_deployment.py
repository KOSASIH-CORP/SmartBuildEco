import json
from kubernetes import client, config

class ClimateResilienceDeployment:
    def __init__(self, deployment_config):
        self.deployment_config = deployment_config
        self.kube_config = config.load_kube_config()

    def deploy(self):
        # Create a Kubernetes deployment
        api = client.AppsV1Api()
        deployment = client.V1Deployment()
        deployment.metadata = client.V1ObjectMeta(name="climate-resilience")
        deployment.spec = client.V1DeploymentSpec(
            replicas=3,
            selector=client.V1LabelSelector(match_labels={"app": "climate-resilience"}),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "climate-resilience"}),
                spec=client.V1PodSpec(containers=[
                    client.V1Container(
                        name="climate-resilience",
                        image="climate-resilience:latest",
                        ports=[client.V1ContainerPort(container_port=80)]
                    )
                ])
            )
        )
        api.create_namespaced_deployment(namespace="default", body=deployment)

    def undeploy(self):
        # Delete a Kubernetes deployment
        api = client.AppsV1Api()
        api.delete_namespaced_deployment(name="climate-resilience", namespace="default")

# Example usage
deployment_config = {
    "image": "climate-resilience:latest",
    "replicas": 3
}

climate_resilience_deployment = ClimateResilienceDeployment(deployment_config)
climate_resilience_deployment.deploy()
