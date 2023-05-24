import adal
import requests

client_id = 'e26babac-f1b9-44b5-af67-a28887ae2978' 
username = 'pbi@in516ht.com'
client_secret = 'cSL8Q~_X4joIlH1rbShj6fSvgS-hRFbeJG4PZbmq'
report_id = '745405bd-c702-481b-9e5d-bb3dfc1cc93d'
workspace_id = '418fc146-6f6a-4b64-afc8-d8856a0d5b6f'

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
access_token = ""
# Check if the request was successful
if response.status_code == 200:
    # Extract the access token from the response
    access_token = response.json()['access_token']
    # print(f'Access token: {access_token}')
else:
    # Print the error message
    print('Error:', response.text)

# Define the Embed URL
embed_url = 'https://app.powerbi.com/reportEmbed?reportId={}'.format(report_id)

# Define the Azure AD authentication parameters
tenant_id = '5630a8c5-5df5-4148-be98-8b60dd9abfd5'
resource = 'https://analysis.windows.net/powerbi/api'

#api_url = https://api.powerbi.com/v1.0/myorg/groups/418fc146-6f6a-4b64-afc8-d8856a0d5b6f/reports/745405bd-c702-481b-9e5d-bb3dfc1cc93d/GenerateToken
# Define the API URL for getting the embed token
api_url = f'https://api.powerbi.com/v1.0/myorg/groups/{workspace_id}/reports/{report_id}/GenerateToken'
print(access_token)
# Define the headers and payload for the API request
headers = {
    'Authorization': f'Bearer{access_token}', 
    'Content-Type': 'application/json'
    }
payload = {
    'accessLevel': 'View',
    'allowEdit': True,
}

# Send the API request to get the embed token
response = requests.post(api_url, headers=headers, json=payload)
print(response)
print(response.text)

# Get the embed token ID and expiration time from the response data
embed_token = response_data['token']
embed_token_id = response_data['tokenId']
embed_token_expiration = response_data['expiration']
# Authenticate with Azure AD to get an access token
context = adal.AuthenticationContext('https://login.microsoftonline.com/{}'.format(tenant_id))
token = context.acquire_token_with_client_credentials(resource, client_id, client_secret)
access_token = token['accessToken']


embed_url = 'https://app.powerbi.com/reportEmbed?reportId={}'.format(report_id)
embed_token =  "H4sIAAAAAAAEAB1Xxa7FSpL8l7d1S2ZqqRdmZvbOTMfMHs2_z53ep0qqgIzI__nHzt7fnJX__PufA0B2N0v8yBmRB19JZpF-EYwizGig03xkNZJ_IXbKGUXPmGmq4-0KHV4R0rAJgB1hwdzOhBrKOcvvoeqrkEyN1i8gWiTP8JczZaDahHAoOj6E5za6AhEVCYjRDfsBjDObl079-BcNxks9ZqfUf-l-95DR6-IrXrB9P56LKVIrG2_6iydt2QDdpSpN6W7l_Ig-F4jDjxBWfanSYttjDnjlW-8QJU-Ruzp7dwuurdY4p30IylAue5hv1hgFgAS2-EXEuNls_HXd737yTTIZGj7KXZpwRIJy9gSyxNYEVZKvEy7Zeu-QTAElyUNIQoGl6zHMUncg30q53RtWUlrmqyMYMDu1D0JTyWRZruZ4kvW6UAteiF4i5IOryn73EKqV3lXRodV4fDC8CFJ1o6w-nyxTyiXUUjfHjoZ4JXF3imqJ-ySHYE9wvY51fG6GvEw8txmHBDSdp3n8wkTgWA-5EUEeDWH01X0ipgNybctFU7dSRho7nv3Dab6foc-hMhVzZEpVa8waFLYWCtFzlvl201p514hL8Zv5xW8dKk7kkb1gL-tF1SQWFipUstni20MLOQK9wc6BIWtqqM6wZHZhl4xkMFjc9BfEblpFN9eY1rX3pErY4odqCtZAjxFTjxQAOARoGkLGMLFq5M8-4ftqPGr2kKm9W2eG6qsyBoQ4LJ1S37E8WpyxzKaijl7gZGxtC5sdeva0qNJ_0OVX6FdZ0seAEvnv4kWt5e-b-6PRFCyQYI9O8Y7ooG2VzGcanIe1AZxzsF2LKnoPuZ7A2Y7M7UaGdUrCQiiuouxWIzaa8lGFUnWKyuKJ5W9AqunDr3LwTU6vkn5ZlUZ7f082rqVqi-d4pYuw_NYcUtDglt4ijNo6X-EnLBqIlfNB4E01hY81cNK9_q5KH5gLAsp3Fu4YQP-mMnd2yzvyO4jpAXFNHHcL6qOU90L0GklXulfOCLdAPYqu2idj8hwxD--Nc49uMFjTCqzVL24V66uUxRA6lzEHDAYhVmtpRBuQqFXHLRGnyuTkKv1trmnzAqHP2xPUXjtxvO6GqmGbCvBuBE90Tm8Z-QU6br4inEG9fknmKXDHuvRcpXVUvqMwmeGiuxmJAWbGkVNI4NMOlyta79f86gLltXksOkd_kMhBxa_3Qyur8kXeL-RHoG_dnvwUbjFSakMMXDMsBnBFnm9fcprzZgieogrsyGDEWG13TU_GvXIlIu1w4oLMmdyXQ5PqcRLhkR3AfsPfBqtAg7DvQszcPwdFRjUZOewT2gwIPAZpOi6Xo4eDXXxunWRAJQCN66xYzTSNqDdTSiBLbItGiX02BHi-Rn9VjQaoA5yQ6jAsQ750Sgn1WeYhz_SrNlUi1UIJX0MtFtmGp8xEyKOK4lnzzui6rDyZxpraaxz_BF4gCyOnvgqA9dFiCKXl2WVoqKbtZ3jKK1ZGa-y3Ml2-GQJUIdDXcjGzEywJkTb4QIPN3S1pi-jUkVuAHJiWn19miDSEDxg91gjhw-mJEHZQRUb840QizkxATITkrXj8Pu4xlCleXa6IWlHBkS2D5YPNPhm97N6KizRuzRWpe5DWxV_QkHcqb96X7dtlFOlfUPR9Y60m1JxwJcc6n8JJ2xv5_PwJTAmIaCNo5s4vWtqlJ_cK6kXkSi8uAe803gMEWjhYq28GtM0RvazU8WEWZLTP3Z0Td1zcwKCHdFo4rlM4Su6D4JcWK0-elhpXplmBIp0jf54q3YUuN74RIBH-5fQC-hcOgsQRXEZ0eN_8S2jhRHwYlBZnSlmsgoi-5YHZUj4gsGSOjPwrXdpTHDio7Rue_hNovKzOudEeBDHkmljKohhU02jW6VsJkOuo39TtG9LZc5lSu_Onj0Q3qVeKt7HYXceSP_l69Mqa_SV4ZCHWhv2Ix0uLJMljZeiepx2rwYUPw5ipT2SVGumBDP9S92O6CJW9s6gPgnGhJF6wQ79UKYH35ppQ8LniNsEkwP_8Kkqubt8qUxEPT2ZGvpEqImwQgymVspOdxQKiJiUZqx_DOUT3rqgg8QbeFc57Aux3KNFr__s50ozC3QIkOeAs6u9tA2jc_K37e5iQeyGfRDu5iGRruk14vr_IRfjVteiHoiV2E0hLvFAE8Dk4qOwGdKrwaneiZcJRZdv074MCu4gsZTJ30svaliUxEB01FEThQa38R5siOxMzB9wgD4a2ICE5HOGGIsk-FUtBoEn8reSiADpyDwy1vUb8OBTYxi2a89E_JSuXJYZ2euBMRsLAcLZnBmudmvpwlZgAFZQPEidIlmOr_sNiar1l9PaP6CdHtmfTtug-Cqfh2LId-mDjiIjWbd34t21m1Hjhf_kk-x_rnaPDFRzNgPFSlsxqEN3Qh-HjiV6yIXJYJOVKbcSj8YvKpIU-kqZjSoELZsID-Y0WKIXP3BLpEesapytYlxmA3ustEL1oWeQUITuRzVhdce8f8RXHo7Ah9LST8b7XmLUFJLFWxKNwq6ZJR_v0sjlqonVHhSYsj9DzCZwYcZIuKP6BDPuwu99Izhsz12R1WSKAPb8R_mYItJzKH_Nd7eAv5Ku8S_IHTumpWel1__F89Ze1joYBEae28K8azQ2Ax6ax-TebrUth8ud8cwuRDuw___zrH257l2PWqvevOgYeaQWNzeCbV26ruk4MNoArEYHxpNpe-WtxxaJBxhjPO-hPRSPQLYKiMICe9qO321Kr85ix4qNMCMNkcEUnY-CPWk_ZbWr_uoy_ayp2slFbEHttHz9ww4b63srHhZfEifQ_2-NzzAe4sA3uHZk8jngkhqf84mS6IwHus15BgCOAZ-jiph21VarGNRu6TDr40rh0t9F8wtxoiquFCZl1gxyvlhuNYv5tD-X6BqGGy7FWc_YHOByNjA2wfzY370E4KevYVoWGpw3vzCOOvN-MpXz0q2pJn8gDAWy2E51JoPTVYuWbdsO5hDZPGDj6zY8lTcnQMEZR9MwMNNvJvs7zr9eFcPOf_8L8Lm21KeEfyt7FO5WdFhvOikWTf0iPh_X93ymva6bsOLfqb0yteNm95A2bKrZanQ4Bq52YMTY56Ig6Knl5pWMrvEjHtWoppeL7a4DsfW6wjzUGTXBiipAcDfPloHyPaaVTEUnXCh8JC2UiTYhCLZ85heey0XxXk8V6ZNlZexAB3HF-jzzWqwLNrVj2VTJdVQgua9LGoJZA_L7YrnPLEUa5AUyq8NfRIDALnoWljbqZ6t-7N4Kl4xYDEW7UAYwsSC5YWvGRfxJQvT0DASuuJVkZ9Ilhq8piT1QcGjql0GQgxXQwzRhHkTRKbNgYZoRSh47qHE1L7vUuTkhPtTKTlTmKXYSB_N0RQi1aFRKFNJl21igtf31zB9lR0dTwTxYGtalzf7AyNf8_Gf_7f97rf4cuDQAA.eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly9XQUJJLU5PUlRILUVVUk9QRS1yZWRpcmVjdC5hbmFseXNpcy53aW5kb3dzLm5ldCIsImV4cCI6MTY4MzU5MTYzMiwiYWxsb3dBY2Nlc3NPdmVyUHVibGljSW50ZXJuZXQiOnRydWV9"
embed_token_id = "46b9f80d-e2dc-4c9e-b290-056a1d431456"
embed_token_expiration =  "2023-05-09T00:20:32Z"
# Define the headers and payload for the embed request
headers = {'Authorization': f'Bearer{access_token}'}
payload = {
    'accessLevel': 'View',
    'allowEdit': False,
    'embedToken': {
        'token': embed_token,
        'tokenId': embed_token_id,
        'expiration': embed_token_expiration,
    },
}

# Send the embed request and get the embed HTML
response = requests.post(embed_url, headers=headers, json=payload)
print(response)
embed_html = response.text

# Display the embed HTML in your web application
print(embed_html)
