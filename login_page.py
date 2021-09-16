from selenium.webdriver.common.by import By
from lib import Lib

class LoginPage(Lib):
    __EMAIL_TEXTBOX = ''
    __SENHA_TEXTBOX = ''
    __ACESSAR_BUTTON = ''

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
    
    
    