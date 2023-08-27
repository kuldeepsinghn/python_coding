import requests
import datetime


def get_repos(username):
    access_token = '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'
    url = f'https://api.github.com/users/{username}/repos'
    headers = {
        'Authorization': f'Token {access_token}'
    }
    response = requests.get(url, headers=headers)
    my_data = response.json()
    # print(my_data)
    repos = []
    for repo_dict in my_data:
        # print(repo_name['name'])
        repos.append(repo_dict['name'])
    return repos


def get_repo_commits(username, repo_name):
    access_token = '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'
    url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
    headers = {
        'Authorization': f'Token {access_token}'
    }
    response = requests.get(url, headers=headers)
    my_data = response.json()
    # print(my_data)
    # print(len(my_data))
    commits_list = []
    for commit in my_data:
        commit_dict = {
            'sha': commit['sha'],
            'author_name': commit['commit']['author']['name'],
            'date': commit['commit']['author']['date']
        }
        commits_list.append(commit_dict)
    return commits_list


# f = open('result.txt', 'w')
# f.write(str(get_repos(username='kuldeepsinghn')))
# f.write(str(get_repo_commits(username='kuldeepsinghn', repo_name='python_coding')))
# f.close()


current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print("Current date & time : ", current_datetime)

# convert datetime obj to string
str_current_datetime = str(current_datetime)

# create a file object along with extension
file_name = str_current_datetime + ".json"
file = open(file_name, 'w')
# file.write(str(get_repos(username='kuldeepsinghn')))
file.write(str(get_repo_commits(username='kuldeepsinghn', repo_name='python_coding')))
# print("File created : ", file.name)
file.close()
access_commits = get_repo_commits(username='kuldeepsinghn', repo_name='python-')
print(access_commits)
 
print(get_repos(username='kuldeepsinghn'))
