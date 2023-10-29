import requests
# request

# Replace with your GitHub username and personal access token
username = "ritukanwer"

token = "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"

# GitHub API base URL
base_url = "https://api.github.com/user/repos"


# Create a session with authorization headers
session = requests.Session()
session.auth = (username, token)

# List all your repositories
response = session.get(f"{base_url}/user/repos")
# get method restapi
# pdf
# jpeg
# json

reposistory = response.json()
print(reposistory)
# Iterate through your repositories and fetch commits
for i in reposistory:
    print(i)
#     repo_name = repo["name"]
#     commits_url = f"{base_url}/repos/{username}/{repo_name}/commits"
#     response = session.get(commits_url)
#     commits = response.json()
#
#     print(f"Commits in {repo_name} repository:")
#     for commit in commits:
#         print(f"{commit['commit']['author']['name']}: {commit['commit']['message']}")




