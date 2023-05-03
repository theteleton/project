"""
import adal
import pandas as pd
import requests
import json
from pypowerbi.dataset import Column, Table, Dataset
from pypowerbi.client import PowerBIClient

reportId = '745405bd-c702-481b-9e5d-bb3dfc1cc93d'
# you might need to change these, but i doubt it 
authority_url = 'https://login.microsoftonline.com/5630a8c5-5df5-4148-be98-8b60dd9abfd5'
resource_url = 'https://analysis.windows.net/powerbi/api'
api_url = 'https://api.powerbi.com/v1.0/myorg/reports/{reportId}/ExportTo'

# change these to your credentials
client_id = 'e26babac-f1b9-44b5-af67-a28887ae2978' 
username = 'pbi@in516ht.com'
client_secret = 'cSL8Q~_X4joIlH1rbShj6fSvgS-hRFbeJG4PZbmq'

# Authenticate using adal
context = adal.AuthenticationContext(authority=authority_url,
                                     validate_authority=True,
                                     api_version=None)
token = context.acquire_token_with_client_credentials(resource=resource_url, client_id=client_id, client_secret=client_secret)
# get your authentication token
print(token['accessToken'])
"""
report_id = '745405bd-c702-481b-9e5d-bb3dfc1cc93d'
workspace_id = '418fc146-6f6a-4b64-afc8-d8856a0d5b6f'
import requests
import pandas as pd

# Replace with your own values
client_id = 'e26babac-f1b9-44b5-af67-a28887ae2978' 
username = 'pbi@in516ht.com'
client_secret = 'cSL8Q~_X4joIlH1rbShj6fSvgS-hRFbeJG4PZbmq'
scope = 'api://e26babac-f1b9-44b5-af67-a28887ae2978'

# Set up the API endpoint URL
auth_url = 'https://login.microsoftonline.com/5630a8c5-5df5-4148-be98-8b60dd9abfd5/oauth2/token'

# Set the request headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Set the request body
body = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}

# Send the request to the API endpoint
response = requests.post(auth_url, headers=headers, data=body)

# Check if the request was successful
if response.status_code == 200:
    # Extract the access token from the response
    access_token = response.json()['access_token']
    # print(f'Access token: {access_token}')
else:
    # Print the error message
    print('Error:', response.text)
# Replace with your own values
#print(access_token)

export_format = 'csv'
api2_url = 'https://analysis.windows.net/powerbi/api/Dataset.Read.All'
# Set up the API endpoint URL

api_url = f'https://app.powerbi.com/groups/{workspace_id}/reports/{report_id}'
api_url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/reports/{report_id}'
# Set the request headers
api_url = f'https://api.powerbi.com/v1.0/myorg/reports/{report_id}/ExportTo'
headers = {
    'Authorization': f'Bearer{access_token}',
    'Content-Type': 'application/json'
}

# Set the request body
body = {
    'format': ''
    #'settings': {
    #    'locale': 'en-us'
    #}
}
visual_name = "SY VS PY"
group_id = workspace_id
api_url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/datasets/520629f8-b990-45e/e-8675-98cb9c28e903'
api_url = f'https://api.powerbi.com/v1.0/myorg/groups/{group_id}/reports/{report_id}/Visuals/visualName:{visual_name}/ExportData'
# Send the request to the API endpoint
response = requests.post(api_url, headers=headers)
print(response.text)
# Check if the request was successful
if response.status_code == 200:
    print("vleze")
    # Extract the download URL from the response
    #download_url = response.json()['location']

    # Send a GET request to the download URL to download the exported data
    #response = requests.get(download_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the CSV data to a Pandas dataframe
        #data = pd.read_csv(response.content)
        pass
        #print(data)
    else:
        # Print the error message
        print('Error:', response.text)
else:
    # Print the error message
    print('Error:', response.text)
