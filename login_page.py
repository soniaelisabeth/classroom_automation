from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from lib import Lib

class LoginPage(Lib):
    __EMAIL_TEXTBOX =  By.ID, 'username'
    __SENHA_TEXTBOX = By.ID, 'password'
    __ACESSAR_BUTTON = By.CLASS_NAME, 'btn-primary'

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
    
    def fill_login(self, text):...

    def fill_senha(self, text):...

    def click_acessar(self):...
    
    

    