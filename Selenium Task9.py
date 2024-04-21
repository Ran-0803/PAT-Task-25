from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class FormFilling:

    def __init__(self):
        self.url = 'https://www.imdb.com/search/name/'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # Explicit wait
        self.wait = WebDriverWait(self.driver, 20)

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait.until(ec.url_to_be(self.url))

    def quit(self):
        self.driver.quit()

    def fillForm(self):
        self.boot()
        # This code is used to scroll the webpage
        self.driver.execute_script('window.scrollBy(0, 500)')
        # This code is used to Expand the page of  filling form
        self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div["
                                                                  "3]/section/section/div/section/section/div["
                                                                  "2]/div/section/div[2]/div["
                                                                  "1]/div/button/span"))).click()
        # This code is used to find the path and fill the name in the name box
        self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div["
                                                                  "3]/section/section/div/section/section/div["
                                                                  "2]/div/section/div[2]/div[1]/section/div/div["
                                                                  "1]/div[2]/div/div/div/div/div/div/input"))).send_keys(
            "Harry Potter")

        # This code is used to click the see results to do the name search
        self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div[2]/div["
                                                                  "3]/section/section/div/section/section/div["
                                                                  "2]/div/section/div[1]/button"))).is_enabled()



obj = FormFilling()
obj.fillForm()
