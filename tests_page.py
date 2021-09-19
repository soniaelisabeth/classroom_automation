from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from lib import Lib

class TestsPage(Lib):
    'Coloquem os localizadores dos elementos aqui, vai facilitar!'
    URL = 'https://undbclassroom.undb.edu.br'
    __EMAIL_TEXTBOX =  By.ID, 'username'
    __SENHA_TEXTBOX = By.ID, 'password'
    __ACESSAR_BUTTON = By.CLASS_NAME, 'btn-primary'

    def __init__(self, driver):
        self.driver = driver
    
    def ct_001(self, user, password):
        self.open_page(self.URL)
        self.fill(self.__EMAIL_TEXTBOX, user)
        self.fill(self.__SENHA_TEXTBOX, password)
        self.click(self.__ACESSAR_BUTTON)
        assert 'Meus cursos' in self.driver.title
    
    def ct_002(self,):...

    def ct_003(self,):...
    
    def ct_004(self,):...
    
    def ct_005(self,):...
    
    def ct_006(self,):...
    
    def ct_007(self,):...
    
    def ct_008(self,):...
    
    def ct_009(self,):...
    
    def ct_0010(self,):...
    
    def ct_0011(self,):...
    