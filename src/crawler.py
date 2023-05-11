from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

report_id = '745405bd-c702-481b-9e5d-bb3dfc1cc93d'
group_id = '418fc146-6f6a-4b64-afc8-d8856a0d5b6f'
# Set up driver
driver = webdriver.Chrome("./chromedriver")
driver.get(f"https://app.powerbi.com/groups/{group_id}/reports/{report_id}/ReportSection")

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
time.sleep(5)
# Wait for Power BI dashboard to load and navigate to the report
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@class='tile-title' and text()='Pair1_Report_1']")))

report = driver.find_element_by_xpath("//div[@class='tile-title' and text()='Pair1_Report1']")
report.click()

# Wait for report to load and export data from first visual
WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//div[@class='visual-container-repeat']//canvas")))

visual = driver.find_element_by_xpath("//div[@class='visual-container-repeat']//canvas")
driver.execute_script("arguments[0].scrollIntoView();", visual)

WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//span[@title='Export data']")))

export_button = driver.find_element_by_xpath("//span[@title='Export data']")
export_button.click()

WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, "//button[@class='control exportDataDialog-exportButton control-enabled']")))

export_data_button = driver.find_element_by_xpath("//button[@class='control exportDataDialog-exportButton control-enabled']")
export_data_button.click()

# Close the browser
driver.quit()