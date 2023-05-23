from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from processing import ImageProcessing
import time
import os
import shutil

# Set up driver
class Crawler:
    def __init__(self, username, password, group_id, report_id, screenshots_path, data_path, downloads_path):
        self.group_id = group_id
        self.report_id = report_id
        self.username = username
        self.password = password
        self.screenshots_path = screenshots_path
        self.data_path = data_path
        self.downloads_path = downloads_path
    def crawl(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {'download.prompt_for_download': False,
         'download.directory_upgrade': True,
         'safebrowsing.enabled': False}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome("./chromedriver", chrome_options=chrome_options)
        driver.get(f"https://app.powerbi.com/groups/{self.group_id}/reports/{self.report_id}/ReportSection")
        driver.set_window_size(width=1846, height=933)

        time.sleep(5)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "email")))
        email = driver.find_element_by_id("email")
        email.send_keys(self.username)
        driver.find_element_by_id("submitBtn").click()
        time.sleep(6)
        password = driver.find_element_by_id("i0118")
        password.send_keys(self.password)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="idDiv_SAOTCS_Proofs"]/div[1]/div').click()
        time.sleep(6)
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "idTxtBx_SAOTCC_OTC")))
        code = input("Enter two-factor authentication code: ")
        code_input = driver.find_element_by_id("idTxtBx_SAOTCC_OTC")
        code_input.send_keys(code)
        driver.find_element_by_id("idSubmit_SAOTCC_Continue").click()
        time.sleep(6)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(6)

        driver.find_element_by_xpath('//*[@id="zoomValueButton"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="pbi-radio-button-3"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="okButton"]').click()
        time.sleep(1)


        list_of_pages = []
        try:
            driver.find_element_by_xpath('//*[@id="pvExplorationHost"]/div/div/exploration/div/explore-canvas/div/div[2]/outspace-pane/article/div[1]/button[2]').click()
            time.sleep(2)
        except:
            pass
        
        
        try:
            driver.find_element_by_xpath('//*[@id="pageNavBtn"]')
            time.sleep(2)
        except:
            pass
        
        pages = driver.find_elements_by_css_selector('[data-testid="pages-navigation-list-items"]')
        print(pages)
        if len(pages) == 0:
            pages = ["First_(unnamed)_page"]

        total = 0
        last_x = 0
        last_y = 0
        N = len(pages)
        cnt = 0
        for i in range(N):
            
            if i < 1:
                curr_folder = ""
                if pages[i] == "First_(unnamed)_page":
                    curr_folder = f"{self.data_path}/{i}.{pages[i]}"
                else:
                    curr_folder = f"{self.data_path}/{i}.{pages[i].text}"
                os.makedirs(curr_folder)
                try:
                    driver.find_element_by_xpath('//*[@id="collapsePagesPaneBtn"]').click()
                    time.sleep(2)
                except:
                    pass
                driver.save_screenshot(f"{self.screenshots_path}/screenshot{i}.png")
                img_proces = ImageProcessing()
                list_of_vizuals = img_proces.preprocess(f"{self.screenshots_path}/screenshot{i}.png")
                list_of_vizuals = sorted(list_of_vizuals)
                print(list_of_vizuals)

                x_start = last_x
                y_start = last_y
                pos = []
                for (x, y, w, h) in list_of_vizuals:
                    x_new = x + w - 7
                    y_new = y + 7
                    print(x_new, y_new)
                    pos.append((x_new - x_start, y_new - y_start, w, h))
                    x_start = x_new
                    y_start = y_new
            else:
                try:
                    driver.find_element_by_xpath('//*[@id="pageNavBtn"]').click()
                    time.sleep(2)
                except:
                    pass

                pages = driver.find_elements_by_css_selector('[data-testid="pages-navigation-list-items"]')
                print(pages)
                curr_folder = f"{self.data_path}/{i}.{pages[i].text}"
                os.makedirs(curr_folder)
                pages[i].click()
                time.sleep(5)

                try:
                    driver.find_element_by_xpath('//*[@id="collapsePagesPaneBtn"]').click()
                    time.sleep(2)
                except:
                    pass

                driver.save_screenshot(f"{self.screenshots_path}/screenshot{i}.png")
                img_proces = ImageProcessing()
                list_of_vizuals = img_proces.preprocess(f"{self.screenshots_path}/screenshot{i}.png")
                list_of_vizuals = sorted(list_of_vizuals)
                print(list_of_vizuals)

                pos = []
                for (x, y, w, h) in list_of_vizuals:
                    x_new = x + w - 7
                    y_new = y + 7
                    print(x_new, y_new)
                    pos.append((x_new - x_start, y_new - y_start, w, h))
                    x_start = x_new
                    y_start = y_new        
                
            n = len(pos)
            
            for idx in range(n):
                total += 1
                
                (x, y, w, h) = pos[idx]
                print(f"idx = {idx}", x, y, w, h)
                #actions.move_by_offset(x, y).context_click().perform()
                #time.sleep(10)
                #actions.move_by_offset(0, 0).context_click().perform()
                
                (x, y, w, h) = pos[idx]
                
                try:
                    print("vleze")
                    
                    actions = ActionChains(driver)
                    actions.move_by_offset(x, y).click().perform()
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="5"]').click()
                    time.sleep(5)
                    driver.find_element_by_css_selector("pbi-radio-group > span:nth-child(2)").click()
                    time.sleep(3)
                    driver.find_element_by_xpath(f'//*[@id="mat-dialog-{total}"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
                    time.sleep(6)
                    button = driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div")
                    if button.text[:4] != ".csv":
                        button = driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(2) > div")
                    button.click()
                    time.sleep(2)
                    driver.find_element_by_xpath(f'//*[@id="mat-dialog-{total}"]/export-data-dialog/mat-dialog-actions/button[1]').click()
                    time.sleep(10)
                    
                    source_dir = self.downloads_path
                    destination_dir = curr_folder
                    files = os.listdir(source_dir)
                    for file in files:
                        if file[-3:] == "csv":
                            source_file = os.path.join(source_dir, file)
                            destination_file = os.path.join(destination_dir, file)
                            shutil.move(source_file, destination_file)
                            if file == "data.csv":
                                file = f"unnamed{cnt}.csv"
                                cnt += 1
                            os.rename(destination_file, os.path.join(destination_dir, f"{idx}.{file}"))
                    continue
                except:
                    pass

                try:
                    print("vleze2")
                    actions = ActionChains(driver)
                    actions.move_by_offset(0,  -7).click().perform()
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="5"]').click()
                    time.sleep(5)
                    driver.find_element_by_css_selector("pbi-radio-group > span:nth-child(2)").click()
                    time.sleep(3)
                    driver.find_element_by_xpath(f'//*[@id="mat-dialog-{total}"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
                    time.sleep(6)
                    button = driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div")
                    if button.text[:4] != ".csv":
                        button = driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(2) > div")
                    button.click()
                    time.sleep(2)
                    driver.find_element_by_xpath(f'//*[@id="mat-dialog-{total}"]/export-data-dialog/mat-dialog-actions/button[1]').click()
                    time.sleep(10)
                    actions = ActionChains(driver)
                    actions.move_by_offset(0,  10).click().perform()
                    time.sleep(2)
                    source_dir = self.downloads_path
                    destination_dir = curr_folder
                    files = os.listdir(source_dir)
                    for file in files:
                        if file[-3:] == "csv":
                            source_file = os.path.join(source_dir, file)
                            destination_file = os.path.join(destination_dir, file)
                            shutil.move(source_file, destination_file)
                            if file == "data.csv":
                                file = f"unnamed{cnt}.csv"
                                cnt += 1
                            os.rename(destination_file, os.path.join(destination_dir, f"{idx}.{file}"))
                    continue
                except:
                    pass
                
                try:
                    print("vleze3")
                    #if idx == 2:
                        #actions = ActionChains(driver)
                        #actions.move_by_offset(0,  0).context_click().perform()
                        #time.sleep(10)
                    actions = ActionChains(driver)
                    actions.move_by_offset(0, 10).click().perform()
                    time.sleep(2)
                    actions = ActionChains(driver)
                    actions.move_by_offset(0, h).click().perform()
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@id="5"]').click()
                    time.sleep(5)
                    driver.find_element_by_css_selector("pbi-radio-group > span:nth-child(2)").click()
                    time.sleep(3)
                    driver.find_element_by_xpath(f'//*[@id="mat-dialog-{total}"]/export-data-dialog/mat-dialog-content/div[3]/pbi-dropdown/button').click()
                    time.sleep(6)
                    button = driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(3) > div")
                    if button.text[:4] != ".csv":
                        button = driver.find_element_by_css_selector("pbi-dropdown-item:nth-child(2) > div")
                    button.click()
                    time.sleep(2)
                    driver.find_element_by_xpath(f'//*[@id="mat-dialog-{total}"]/export-data-dialog/mat-dialog-actions/button[1]').click()
                    time.sleep(10)
                    actions = ActionChains(driver)
                    actions.move_by_offset(0, -h-10).click().perform()
                    time.sleep(2)
                    source_dir = self.downloads_path
                    destination_dir = curr_folder
                    files = os.listdir(source_dir)
                    for file in files:
                        if file[-3:] == "csv":
                            source_file = os.path.join(source_dir, file)
                            destination_file = os.path.join(destination_dir, file)
                            shutil.move(source_file, destination_file)
                            if file == "data.csv":
                                file = f"unnamed{cnt}.csv"
                                cnt += 1
                            os.rename(destination_file, os.path.join(destination_dir, f"{idx}.{file}"))
                    continue
                except:
                    pass

        time.sleep(10)
        driver.quit()

        
   
        