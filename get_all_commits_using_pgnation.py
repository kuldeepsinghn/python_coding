import requests

# GitHub repository information
owner = "kuldeepsinghn"
repo = "python_coding"

# API endpoint for listing commits
url = f"https://api.github.com/repos/{owner}/{repo}/commits"

# Initialize a list to store all commits
all_commits = []

page = 1
per_page = 100  # You can adjust this based on your needs

while True:
    # Send a GET request to fetch commits for the specified page
    params = {"page": page, "per_page": per_page}
    headers = {"Authorization": "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"}  # Replace with your token
    response = requests.get(url, params=params, headers=headers)

    # Check if there are more commits to fetch
    if response.status_code == 200 and len(response.json()) > 0:
        # Append commits from the current page to the list
        all_commits.extend(response.json())
        page += 1
    else:
        # No more commits to fetch
        break

# Now, all_commits contains all the commits of the repository
print(f"Total commits fetched: {all_commits}")
