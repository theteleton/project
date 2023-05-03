import requests
import json

# Replace with your own values
access_token = 'YOUR_ACCESS_TOKEN'
report_id = '745405bd-c702-481b-9e5d-bb3dfc1cc93d'
workspace_id = '418fc146-6f6a-4b64-afc8-d8856a0d5b6f'

# Set up the API endpoint URL
api_url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/reports/{report_id}/ExportTo'

# Set the request headers
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Set the request body
body = {
    'format': 'pdf',
    'landscape': 'true'
}

# Send the request to the API endpoint
response = requests.post(api_url, headers=headers, data=json.dumps(body))

# Check if the request was successful
if response.status_code == 202:
    # Print the response headers
    print('Request accepted')
    print(response.headers)
else:
    # Print the error message
    print('Error:', response.text)