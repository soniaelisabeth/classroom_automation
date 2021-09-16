from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Lib():
    WEBDRIVER_PATH = '.\\tools\\chromedriver.exe'

    def start_browser(self):
        self.driver = webdriver.Chrome(self.WEBDRIVER_PATH)
        return self.driver

    def click(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator)).click()
    
    def fill(self, locator, text):
        elem = EC.element_to_be_clickable(locator)
        elem = self.webdriver.wait.until(elem)
        elem.clear()
        elem.send_keys(text)
