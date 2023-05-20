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


# Set up driver
class Crawler:
    def __init__(self, username, password, group_id, report_id):
        self.group_id = group_id
        self.report_id = report_id
        self.username = username
        self.password = password
    
    def crawl(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.prompt_for_download': False,
         'download.directory_upgrade': True,
         'safebrowsing.enabled': False}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
        driver.get(f"https://app.powerbi.com/groups/{self.group_id}/reports/{self.report_id}/ReportSection")
        driver.maximize_window()

        time.sleep(5)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
        email = driver.find_element_by_id("email")
        email.send_keys(self.username)
        driver.find_element_by_id("submitBtn").click()
        time.sleep(5)
        password = driver.find_element_by_id("i0118")
        password.send_keys(self.password)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div').click()
        time.sleep(5)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "idTxtBx_SAOTCC_OTC")))
        code = input("Enter two-factor authentication code: ")
        code_input = driver.find_element_by_id("idTxtBx_SAOTCC_OTC")
        code_input.send_keys(code)
        driver.find_element_by_id("idSubmit_SAOTCC_Continue").click()
        time.sleep(10)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(10)

        actions = ActionChains(driver)
        actions.move_by_offset(961, 121).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="5"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
        time.sleep(6)
        driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-dialog-0"]/export-data-dialog/mat-dialog-actions/button[1]').click()
        time.sleep(5)

        actions = ActionChains(driver)
        actions.move_by_offset(0, 120).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="5"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mat-dialog-1"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
        time.sleep(6)
        driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div").click()

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-dialog-1"]/export-data-dialog/mat-dialog-actions/button[1]').click()
        time.sleep(5)

        actions = ActionChains(driver)
        actions.move_by_offset(0, 285).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="5"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mat-dialog-2"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
        time.sleep(6)
        driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-dialog-2"]/export-data-dialog/mat-dialog-actions/button[1]').click()
        time.sleep(5)

        
        actions = ActionChains(driver)
        actions.move_by_offset(700, -55).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="5"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mat-dialog-3"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
        time.sleep(6)
        driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-dialog-3"]/export-data-dialog/mat-dialog-actions/button[1]').click()
        time.sleep(15)

        actions = ActionChains(driver)
        actions.move_by_offset(0, -341).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="5"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mat-dialog-4"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
        time.sleep(6)
        driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-dialog-4"]/export-data-dialog/mat-dialog-actions/button[1]').click()
        time.sleep(5)

        driver.find_element_by_xpath('//*[@id="content"]/div/report/exploration-container/div/div/docking-container/div/div/exploration-fluent-navigation/section/mat-action-list/button[2]').click()

        time.sleep(10)

        actions = ActionChains(driver)
        actions.move_by_offset(-696, 0).click().perform()
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="5"]').click()
        time.sleep(10)
        driver.find_element_by_xpath('//*[@id="mat-dialog-5"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
        time.sleep(6)
        driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-dialog-5"]/export-data-dialog/mat-dialog-actions/button[1]').click()
        time.sleep(10)

        actions = ActionChains(driver)
        actions.move_by_offset(0, 111).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="5"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mat-dialog-6"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
        time.sleep(6)
        driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-dialog-6"]/export-data-dialog/mat-dialog-actions/button[1]').click()
        time.sleep(5)

        actions = ActionChains(driver)
        actions.move_by_offset(0, 285).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="5"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mat-dialog-7"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
        time.sleep(6)
        driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-dialog-7"]/export-data-dialog/mat-dialog-actions/button[1]').click()
        time.sleep(5)

        actions = ActionChains(driver)
        actions.move_by_offset(695, -58).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="5"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mat-dialog-8"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
        time.sleep(6)
        driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-dialog-8"]/export-data-dialog/mat-dialog-actions/button[1]').click()
        time.sleep(15)

        actions = ActionChains(driver)
        actions.move_by_offset(0, -341).click().perform()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="5"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="mat-dialog-9"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
        time.sleep(6)
        driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-dialog-9"]/export-data-dialog/mat-dialog-actions/button[1]').click()
        time.sleep(5)
        driver.quit()