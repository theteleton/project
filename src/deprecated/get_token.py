import requests
import json

# Replace with your own values
client_id = '5630a8c5-5df5-4148-be98-8b60dd9abfd5'
client_secret = '71f2aa02-015d-4967-90fe-cac230e5808c'
scope = 'https://analysis.windows.net/powerbi/api/App.Read.All'

# Set up the API endpoint URL
auth_url = 'https://api.powerbi.com/v1.0/myorg/GenerateToken'

# Set the request headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Set the request body
body = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': scope
}

# Send the request to the API endpoint
response = requests.post(auth_url, headers=headers, data=body)
print(response.status_code)
# Check if the request was successful
if response.status_code == 200:
    # Extract the access token from the response
    access_token = response.json()['access_token']
    print(f'Access token: {access_token}')
else:
    # Print the error message
    print('Error:', response.text)