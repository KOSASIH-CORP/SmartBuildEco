import os
import json
from github import Github

class Packages:
    def __init__(self, repo):
        self.repo = repo
        self.g = Github()

    def create_package(self, package_name):
        # Create a GitHub Package
        self.repo.create_package(package_name, "Create a new package")

    def upload_package(self, package_name, file_path):
        # Upload a package to GitHub
        package = self.g.get_package(package_name)
        package.upload(file_path)

# Example usage
repo = Github().get_repo("KOSASIH-CORP/SmartBuildEco")
packages = Packages(repo)
packages.create_package("my-package")
packages.upload_package("my-package", "path/to/file.zip")
