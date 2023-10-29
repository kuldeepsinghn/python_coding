# import requests
# import datetime
#
#
# def get_repos(username):
#     access_token = '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'
#     url = f'https://api.github.com/users/{username}/repos'
#     headers = {
#         'Authorization': f'Token {access_token}'
#     }
#     response = requests.get(url, headers=headers)
#     my_data = response.json()
#     # print(my_data)
#     repos = []
#     for repo_dict in my_data:
#         # print(repo_name['name'])
#         repos.append(repo_dict['name'])
#     return repos
#
#
# # def get_repo_commits(username, repo_name):
# #     access_token = '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'
# #     url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
# #     headers = {
# #         'Authorization': f'Token {access_token}'
# #     }
# #     response = requests.get(url, headers=headers)
# #     my_data = response.json()
# #     # print(my_data)
# #     # print(len(my_data))
# #     commits_list = []
# #     for commit in my_data:
# #         commit_dict = {
# #             'sha': commit['sha'],
# #             'author_name': commit['commit']['author']['name'],
# #             'date': commit['commit']['author']['date']
# #         }
# #         commits_list.append(commit_dict)
# #     return commits_list
#
# def fetch_commits_by_pgnation(owner,repo):
#     # API endpoint for listing commits
#     url = f"https://api.github.com/repos/{owner}/{repo}/commits"
#     access_token = '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'
#
#     all_commits = []
#
#     page = 1
#     per_page = 10  # You can adjust this based on your needs
#
#     while True:
#         # Send a GET request to fetch commits for the specified page
#         params = {"page": page, "per_page": per_page}
#         headers = {
#             'Authorization': f'Token {access_token}'
#         }
#         response = requests.get(url, params=params, headers=headers)
#         my_data = response.json()
#
#         # Check if there are more commits to fetch
#         if len(response.json()) > 0:
#             # Append commits from the current page to the list
#             for commit in my_data:
#                 # print(commit)
#                 # print((commit['sha'], commit['commit']['author']['name'], commit['commit']['author']['date']))
#                 commit_dict = {
#                     'sha': commit['sha'],
#                     'author_name': commit['commit']['author']['name'],
#                     'date': commit['commit']['author']['date']
#                 }
#                 all_commits.append(commit_dict)
#             # all_commits.extend(my_data)
#             page += 1
#         else:
#             # No more commits to fetch
#             break
#
#     return all_commits
#
# # f = open('result.txt', 'w')
# # f.write(str(get_repos(username='kuldeepsinghn')))
# # f.write(str(get_repo_commits(username='kuldeepsinghn', repo_name='python_coding')))
# # f.close()
#
#
# current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# print("Current date & time : ", current_datetime)
#
# # convert datetime obj to string
# str_current_datetime = str(current_datetime)
#
# # create a file object along with extension
# file_name = str_current_datetime + ".json"
# file = open(file_name, 'w')
# # file.write(str(get_repos(username='kuldeepsinghn')))
# # file.write(str(get_repo_commits(username='kuldeepsinghn', repo_name='python_coding')))
# file.write(str(fetch_commits_by_pgnation(owner='kuldeepsinghn', repo='python_coding')))
# file.write(str(len(fetch_commits_by_pgnation(owner='kuldeepsinghn', repo='python_coding'))))
# # print("File created : ", file.name)
# file.close()
# access_commits = fetch_commits_by_pgnation(owner='kuldeepsinghn', repo='python_coding')
# print(len(access_commits))
#
# # print(get_repos(username='kuldeepsinghn'))
# # print(get_repos(username='kuldeepsinghn'))


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
        # print(repo_dict)
        # print(repo_name['name'])
        repos.append(repo_dict['name'])
    return repos


# def get_repo_commits(username, repo_name):
#     access_token = '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'
#     url = f'https://api.github.com/repos/{username}/{repo_name}/commits'
#     headers = {
#         'Authorization': f'Token {access_token}'
#     }
#     response = requests.get(url, headers=headers)
#     my_data = response.json()
#     # print(my_data)
#     # print(len(my_data))
#     commits_list = []
#     for commit in my_data:
#         commit_dict = {
#             'sha': commit['sha'],
#             'author_name': commit['commit']['author']['name'],
#             'date': commit['commit']['author']['date']
#         }
#         commits_list.append(commit_dict)
#     return commits_list

def fetch_commits_by_pgnation(owner, repo):
    # API endpoint for listing commits
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    access_token = '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'

    all_commits = []

    page = 1
    per_page = 10  # You can adjust this based on your needs

    while True:
        # Send a GET request to fetch commits for the specified page
        params = {"page": page, "per_page": per_page}
        headers = {
            'Authorization': f'Token {access_token}'
        }
        response = requests.get(url, params=params, headers=headers)
        my_data = response.json()
        # print(my_data)

        # Check if there are more commits to fetch
        if len(response.json()) > 0:
            # Append commits from the current page to the list
            for commit in my_data:
                print(commit)
                # print((commit['sha'], commit['commit']['author']['name'], commit['commit']['author']['date']))
                commit_dict = {
                    'sha': commit['sha'],
                    'author_name': commit['commit']['author']['name'],
                    'date': commit['commit']['author']['date']
                }
                all_commits.append(commit_dict)
            # all_commits.extend(my_data)
            page += 1
        else:
            # No more commits to fetch
            break

    return all_commits


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
# file.write(str(get_repo_commits(username='kuldeepsinghn', repo_name='python_coding')))
file.write(str(fetch_commits_by_pgnation(owner='kuldeepsinghn', repo='python_coding')))
file.write(str(len(fetch_commits_by_pgnation(owner='kuldeepsinghn', repo='python_coding'))))
# print("File created : ", file.name)
file.close()
access_commits = fetch_commits_by_pgnation(owner='kuldeepsinghn', repo='python_coding')
print(len(access_commits))

print(get_repos(username='kuldeepsinghn'))
# print(get_repos(username='kuldeepsinghn'))
