import requests

import json
import base64

# Load the access token from the JSON file
with open('config.json') as config_file:
    config = json.load(config_file)

client_id = config['client_id']
client_secret = config['client_secret']

# Define the token URL
token_url = 'https://api-m.sandbox.paypal.com/v1/oauth2/token'

# Define the grant type for client credentials
grant_type = 'client_credentials'

# Create the authentication string by base64 encoding the client ID and client secret
auth_string = f"{client_id}:{client_secret}"
encoded_auth = base64.b64encode(auth_string.encode()).decode()

# Set the headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': f'Basic {encoded_auth}',
}

# Set the data for the POST request
data = {
    'grant_type': grant_type,
}

# Send the POST request to obtain the access token
response = requests.post(token_url, headers=headers, data=data)

if response.status_code == 200:
    access_token_data = response.json()
    access_token = access_token_data.get('access_token')
    print("Access Token:", access_token)
else:
    print('Failed to obtain access token. Status code:', response.status_code)
    print('Response content:', response.text)