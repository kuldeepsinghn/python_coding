# import requests
#
#
# def Get_states_data():
#     url = "https://api.covid19india.org/data.json"
#
#     # Make a GET request to the API endpoint
#     response = requests.get(url)
#
#     data = response.json()
#     # print(data)
#     state_data = []
#     # for i in data:
#     #     print(i)
#     for states in data["statewise"]:
#         # print(states)
#         if states['state'] == "Rajasthan":
#             rajasthan_dict = {
#                 "State ": states['state'],
#                 "Total Confirmed Cases": states["confirmed"],
#                 "Total Recovered Cases" :states["recovered"],
#                 "Total Deaths": states["deaths"],
#                 "Active Cases": states["active"],
#                 "Statecode": states['statecode'],
#                 "Last Updated date and time": states["lastupdatedtime"]
#             }
#             state_data.append(rajasthan_dict)
#     return state_data
#
#
# # x=Get_states_data()
# # print(x)
#
#
# def Get_district_data():
#     # api_url = "https://api.covid19india.org/data.json"
#     url = "https://data.covid19india.org/v4/min/data.min.json"
#
#     response = requests.get(url)
#
#     data = response.json()
#     print((data))
#     # for i in data:
#     #     print(i)
#     # for states in data["RJ"]["districts"]:
#     #     if states["RJ"]["districts"]== "Jaipur":
#     #         district_data={
#     #             "delta": states['RJ']["districts"]['delta']
#     #         }
#     # return district_data
#
#
# Get_district_data()



import requests
import base64

# Spotify API credentials from your Spotify Developer Dashboard
client_id = '23dee45ab4e344a9a75df4b7ef509781'
client_secret = '769348b820004d15a9d3586bb726fba4'
redirect_uri = 'https://api.spotify.com/v1/playlists/{playlist_id}'  # Must match the one set in your Spotify Developer Dashboard

# Define the scope (permissions)
scope = 'playlist-read-private playlist-read-collaborative'

# Step 1: Redirect the user for authorization (OAuth 2.0)
authorization_url = f'https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri={redirect_uri}&scope={scope}'

print('Please visit this URL to authorize your application:', authorization_url)
authorization_code = input('Enter the authorization code from the redirect URI: ')

# Step 2: Exchange the authorization code for an access token
token_url = 'https://accounts.spotify.com/api/token'

# Encode the client ID and client secret to create the authorization header
client_credentials = f'{client_id}:{client_secret}'
base64_client_credentials = base64.b64encode(client_credentials.encode()).decode()
headers = {
    'Authorization': f'Basic {base64_client_credentials}',
}

data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri,
}

# Make a POST request to obtain the access token
response = requests.post(token_url, data=data, headers=headers)

if response.status_code == 200:
    token_data = response.json()
    access_token = token_data['access_token']

    # Step 3: Use the access token to make API requests
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    # Get the current user's playlists
    playlists_url = 'https://api.spotify.com/v1/me/playlists'
    playlists_response = requests.get(playlists_url, headers=headers)

    if playlists_response.status_code == 200:
        playlists_data = playlists_response.json()
        for playlist in playlists_data['items']:
            print(f"Playlist Name: {playlist['name']}")
            print(f"Playlist ID: {playlist['id']}")
            print("\n")
    else:
        print('Error:', playlists_response.status_code, playlists_response.text)

else:
    print('Error:', response.status_code, response.text)
