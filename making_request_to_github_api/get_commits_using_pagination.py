import requests


def fetch_commits_by_pgnation(owner,repo):
    # API endpoint for listing commits
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    access_token = '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'

    # Initialize a list to store all commits
    all_commits = []

    page = 1
    per_page = 30  # You can adjust this based on your needs

    while True:
        # Send a GET request to fetch commits for the specified page
        params = {"page": page, "per_page": per_page}
        headers = {
            'Authorization': f'Token {access_token}'
        }
        response = requests.get(url, params=params, headers=headers)
        my_data = response.json()

        # Check if there are more commits to fetch
        if len(response.json()) > 0:
            # Append commits from the current page to the list
            for commit in my_data:
                # print(commit)
                # print((commit['sha'], commit['commit']['author']['name'], commit['commit']['author']['date']))
                commit_dict = {
                    'sha': commit['sha'],
                    'author_name': commit['commit']['author']['name'],
                    'date': commit['commit']['author']['date']
                }
                all_commits.append(commit_dict)
            page += 1
        else:
            # No more commits to fetch
            break

    return all_commits


all_commits_of_repo = fetch_commits_by_pgnation(owner='ritukanwer',repo='python_')
print((all_commits_of_repo))
