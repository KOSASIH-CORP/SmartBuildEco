import os
import json
from github import Github

class Actions:
    def __init__(self, repo):
        self.repo = repo
        self.g = Github()

    def create_workflow(self, workflow_file):
        # Create a GitHub Actions workflow
        self.repo.create_file(workflow_file, "Create a new workflow")

    def run_workflow(self, workflow_id):
        # Run a GitHub Actions workflow
        workflow = self.g.get_workflow(workflow_id)
        workflow.dispatch()

# Example usage
repo = Github().get_repo("KOSASIH-CORP/SmartBuildEco")
actions = Actions(repo)
actions.create_workflow("my_workflow.yml")
actions.run_workflow("1234567890")
