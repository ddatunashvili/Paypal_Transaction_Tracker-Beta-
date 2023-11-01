import requests
import base64

# Replace 'YOUR_CLIENT_ID' and 'YOUR_CLIENT_SECRET' with your actual PayPal API credentials
client_id = 'AWHDGis0lQdYufhP6i3-OPOfX1dTP6iqIAk-ek70MUuDreR-MvVon8QpUZ66D1h43nX3gfQFedwt3Fss'
client_secret = 'EEAJqFjXFNoOJHI_hm45pDB_WgTcB90PEc9nCTY5owfxIe4fT2HYBAE-J8jaPEnj7O5bdAVg8rTJKa4S'

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

# Check if the access token was successfully obtained
if response.status_code == 200:
    access_token_data = response.json()
    access_token = access_token_data.get('access_token')
    print("Access Token:", access_token)

    # Use the access token to make a request for transactions
    transaction_url = 'https://api-m.sandbox.paypal.com/v1/reporting/transactions'

    # Define the parameters for the transaction request
    transaction_params = {
        'start_date': '2023-01-01T00:00:00-0700',
        'end_date': '2023-12-31T23:59:59-0700',
        'fields': 'all',
        'page_size': '100',
        'page': '1',
    }

    # Set the headers for the transaction request
    transaction_headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }

    # Send the request to retrieve transaction history
    transaction_response = requests.get(transaction_url, headers=transaction_headers, params=transaction_params)

    if transaction_response.status_code == 200:
        transaction_data = transaction_response.json()
        # Process the transaction data as needed
        print("Transaction Data:", transaction_data)
    else:
        print('Failed to retrieve transactions. Status code:', transaction_response.status_code)
        print('Response content:', transaction_response.text)

else:
    print('Failed to obtain access token. Status code:', response.status_code)
    print('Response content:', response.text)
