from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
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
# Set up the webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("user-agent=fri-ids-HW1-student1")
driver = webdriver.Chrome("./chromedriver", options=chrome_options)

driver.get('https://app.powerbi.com/')
wait = WebDriverWait(driver, 10)

# Log in to Power BI using access token
access_token = '<your_access_token>'
driver.execute_script(f"localStorage.setItem('powerbiAccessToken','{access_token}');")
driver.refresh()

# Navigate to the report and select the visual
report_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Pair1_Report1')))
report_link.click()
visual_title = wait.until(EC.presence_of_element_located((By.XPATH, f'//div[text()="SY VS PY"]')))
visual_title.click()

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