import requests

def python_coding():
    username = 'kuldeepsinghn'
    repo_name = 'python_coding'
    access_token = 'xxx'
    url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
    headers = {
        'Authorization': f'Token {access_token}'
    }
    response = requests.get(url, headers=headers)
    my_data = response.json()

    # print(my_data)
    # print(len(my_data))
    commits_list=[]
    for commit in my_data:
        # print(commit)
        # print((commit['sha'], commit['commit']['author']['name'], commit['commit']['author']['date']))
        commit_dict = {
            'sha': commit['sha'],
            'author_name': commit['commit']['author']['name'],
            'date': commit['commit']['author']['date']
        }
        commits_list.append(commit_dict)
    return commits_list
# 1a3de8e607feaed23ccb214f9f772eb8259cb159
x=python_coding()
print(x)


