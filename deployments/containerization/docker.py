import os
import docker

class DockerContainer:
    def __init__(self, image, command):
        self.image = image
        self.command = command
        self.client = docker.from_env()

    def run(self):
        # Run a Docker container
        container = self.client.containers.run(self.image, self.command, detach=True)
        return container

    def stop(self, container_id):
        # Stop a Docker container
        container = self.client.containers.get(container_id)
        container.stop()

    def remove(self, container_id):
        # Remove a Docker container
        container = self.client.containers.get(container_id)
        container.remove()

# Example usage
image = "my-image:latest"
command = "python app.py"
docker_container = DockerContainer(image, command)
container_id = docker_container.run()
print(container_id)

docker_container.stop(container_id)
docker_container.remove(container_id)
