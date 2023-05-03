from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import requests
import pandas as pd

import os

os.chmod('./chromedriver', 755) 
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
# Set up the webdriver
print(access_token)
report_id = '745405bd-c702-481b-9e5d-bb3dfc1cc93d'
workspace_id = '418fc146-6f6a-4b64-afc8-d8856a0d5b6f'
tenantID = '5630a8c5-5df5-4148-be98-8b60dd9abfd5'
chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=fri-project-student1")
driver = webdriver.Chrome("./chromedriver", options=chrome_options)
driver.get(f'https://login.microsoftonline.com/{tenantID}/oauth2/v2.0/token')
#driver.get(f'https://app.powerbi.com/groups/{workspace_id}/reports/{report_id}&accessToken={access_token}/ReportSection')
wait = WebDriverWait(driver, 10)

# Log in to Power BI using access token
#driver.execute_script(f"localStorage.setItem('powerbiAccessToken','{access_token}');")
#driver.refresh()

# Wait for the report to load
driver.implicitly_wait(10)

# Select the visual
visual_title = driver.find_element_by_xpath('//div[text()="<your_visual_name>"]')
visual_title.click()

# Export the data
export_menu = driver.find_element_by_css_selector('button[data-icon-name="ExportData"]')
export_menu.click()
csv_button = driver.find_element_by_xpath('//button[text()="CSV"]')
csv_button.click()

# Export the data
export_menu = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-icon-name="ExportData"]')))
export_menu.click()
csv_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="CSV"]')))
csv_button.click()

# Wait for the download to finish
wait.until(lambda driver: len(driver.window_handles) == 2)
driver.switch_to.window(driver.window_handles[1])
wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

# Save the CSV file
with open('visual_data.csv', 'wb') as f:
    f.write(driver.page_source.encode('utf-8'))

# Close the webdriver
driver.quit()