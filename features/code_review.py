import os
import json
from github import Github

class CodeReview:
    def __init__(self, repo):
        self.repo = repo
        self.g = Github()

    def create_pull_request(self, pull_request_title):
        # Create a GitHub Pull Request
        self.repo.create_pull_request(pull_request_title, "Create a new pull request")

    def approve_pull_request(self, pull_request_id):
        # Approve a GitHub Pull Request
        pull_request = self.g.get_pull_request(pull_request_id)
        pull_request.approve()

# Example usage
repo = Github().get_repo("KOSASIH-CORP/SmartBuildEco")
code_review = CodeReview(repo)
code_review.create_pull_request("Update README.md")
code_review.approve_pull_request("1234567890")
