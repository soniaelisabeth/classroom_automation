from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from lib import Lib

class TestsPage(Lib):
    'Coloquem os localizadores dos elementos aqui, vai facilitar!'
    __EMAIL_TEXTBOX =  By.ID, 'username'
    __SENHA_TEXTBOX = By.ID, 'password'
    __ACESSAR_BUTTON = By.CLASS_NAME, 'btn-primary'

    def __init__(self, driver):
        self.driver = driver
    
    def ct_001(self, user, password):
        self.fill(self.__EMAIL_TEXTBOX, user)
        self.fill(self.__SENHA_TEXTBOX, password)
        self.click(self.__ACESSAR_BUTTON)
        assert 'Meus cursos' in self.driver.title

    