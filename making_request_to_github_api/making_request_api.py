
import requests

# GitHub username you want to fetch information for
username = 'kuldeepsinghn'
repo_name='python_coding'

# your GitHub Personal Access Token
access_token = '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'
# access_token = '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'

# The URL of the GitHub API endpoint for the specific user
url = f'https://api.github.com/users/{username}/repos'
# url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
# commit sha and time stamp, owner-->list of dict
# create a fucntions (input repo name)
# get all the commits (pgnation)

# Set up the headers with the authorization token
headers = {
    'Authorization': f'Token {access_token}'
}

# Make the GET request
response = requests.get(url, headers=headers)
my_data = response.json()
# print(len(my_data))
print(my_data)
# print(len(my_data))
commits_list=[]
for commit in my_data:
    repo_name=commit['name']
    print(repo_name)
    print( commit['commit']['author']['name'], commit['commit']['author']['date']))
    print((commit['sha'], commit['commit']['author']['name'], commit['commit']['author']['date']))
#     commit_dict = {
#         'sha': commit['sha'],
#         'author_name': commit['commit']['author']['name'],
#         'date': commit['commit']['author']['date']
#     }
#     commits_list.append(commit_dict)
# print(commits_list)
#
#     print( (i['sha'],i['commit']['author']['name'],i['commit']['author']['date']))
# for repo in my_data:
#     # repo_name= repo['name']['python_coding']
#     print(repo_name)
