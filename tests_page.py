from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from lib import Lib

class TestsPage(Lib):
    'Coloquem os localizadores dos elementos aqui, vai facilitar!'
    URL = 'https://undbclassroom.undb.edu.br'
    __EMAIL_TEXTBOX =  By.ID, 'username'
    __SENHA_TEXTBOX = By.ID, 'password'
    __ACESSAR_BUTTON = By.CLASS_NAME, 'btn-primary'
    __ESQUECEU_SENHA_BUTTON = By.XPATH, '//a[contains(text(), "Esqueceu o seu usuário ou senha?")]'
    __ID_USUARIO_TEXTBOX = By.ID, 'id_username'
    __BUSCAR_BUTTON = By.NAME, 'submitbuttonusername'

    def __init__(self, driver):
        self.driver = driver
    
    def ct_001(self, user, password):
        #Teste de login
        self.open_page(self.URL)
        self.fill(self.__EMAIL_TEXTBOX, user)
        self.fill(self.__SENHA_TEXTBOX, password)
        self.click(self.__ACESSAR_BUTTON)
        assert 'Meus cursos' in self.driver.title
    
    def ct_002(self, user):
        #Alteração de usuário ou senha pela identificação do usuário
        self.open_page(self.URL)
        self.click(self.__ESQUECEU_SENHA_BUTTON)
        self.fill(self.__ID_USUARIO_TEXTBOX, user)
        self.click(self.__BUSCAR_BUTTON)
        text = 'Se o usuário e o email estiverem corretos um email deve ter sido enviado a você.'
        assert text in self.driver.title

    def ct_003(self,):...
    
    def ct_004(self,):...
    
    def ct_005(self,):...
    
    def ct_006(self,):...
    
    def ct_007(self,):...
    
    def ct_008(self,):...
    
    def ct_009(self,):...
    
    def ct_0010(self,):...
    
    def ct_0011(self,):...
    