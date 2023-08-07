import os
import base64
import requests
from github import Github

# GitHub repository information
repo_owner = "kushalpatel2210"
repo_name = "LeetCode"
branch_name = "main"  # Change to your default branch name
file_path = "README.md"

# Fetch folder names
folder_names = os.popen("python get_folders.py").read().strip().split('\n')

# Construct updated content
new_content = "## Solved LeetCode Problems\n"
for folder in folder_names:
    new_content += f"- {folder}\n"

# Get GitHub API token from environment variable
github_token = os.environ["GITHUB_TOKEN"]

# Initialize GitHub repository and get existing README content
g = Github(github_token)
repo = g.get_repo(f"{repo_owner}/{repo_name}")
readme = repo.get_contents(file_path, ref=branch_name)
old_content = base64.b64decode(readme.content).decode("utf-8")

# Update README content and push changes
if new_content != old_content:
    new_content_base64 = base64.b64encode(new_content.encode("utf-8")).decode("utf-8")
    payload = {
        "message": "Update README with folder names",
        "content": new_content_base64,
        "sha": readme.sha,
        "branch": branch_name
    }
    headers = {"Authorization": f"Bearer {github_token}"}
    response = requests.put(f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}", json=payload, headers=headers)

    if response.status_code == 200:
        print("README updated successfully.")
    else:
        print("Error updating README:", response.text)
else:
    print("No changes needed in README.")
