from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

report_id = '745405bd-c702-481b-9e5d-bb3dfc1cc93d'
group_id = '418fc146-6f6a-4b64-afc8-d8856a0d5b6f'
# Set up driver

driver = webdriver.Chrome("./chromedriver")
driver.get(f"https://app.powerbi.com/groups/{group_id}/reports/{report_id}/ReportSection")
driver.maximize_window()

time.sleep(5)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
# Enter email and password
email = driver.find_element_by_id("email")
email.send_keys("pbi@in516ht.com")
driver.find_element_by_id("submitBtn").click()
time.sleep(5)

password = driver.find_element_by_id("i0118")
password.send_keys("7rTMTgw#BFBPR*WU")
driver.find_element_by_id("idSIButton9").click()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div').click()
time.sleep(5)
# Click on Next button

# Wait for two-factor authentication page to load and enter code
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "idTxtBx_SAOTCC_OTC")))

code = input("Enter two-factor authentication code: ")
code_input = driver.find_element_by_id("idTxtBx_SAOTCC_OTC")
code_input.send_keys(code)

# Click on Verify button
driver.find_element_by_id("idSubmit_SAOTCC_Continue").click()
time.sleep(10)
driver.find_element_by_id("idSIButton9").click()
time.sleep(10)


actions = ActionChains(driver)
actions.move_by_offset(949, 128).click().perform()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="5"]').click()

time.sleep(5)
driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/export-data-dialog/mat-dialog-actions/button[1]').click()

time.sleep(10)
# Close the browser
driver.quit()