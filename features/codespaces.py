import os
import json
from github import Github

class Codespaces:
    def __init__(self, repo):
        self.repo = repo
        self.g = Github()

    def create_codespace(self, codespace_name):
        # Create a GitHub Codespace
        self.repo.create_codespace(codespace_name, "Create a new codespace")

    def start_codespace(self, codespace_id):
        # Start a GitHub Codespace
        codespace = self.g.get_codespace(codespace_id)
        codespace.start()

# Example usage
repo = Github().get_repo("KOSASIH-CORP/SmartBuildEco")
codespaces = Codespaces(repo)
codespaces.create_codespace("my-codespace")
codespaces.start_codespace("1234567890")
