import requests
import json
username = "ksn"
url = "https://api.github.com/users/{}".format(username)
response =requests.get(url)
# print(response.text)
output = json.loads(response.text)
# print(output['avatar_url'])

response_img = requests.get(output['avatar_url'])

# print(response.content)
fp = open('{}.png'.format(username),"wb")
fp.write(response.content)
fp.close()


