from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from lib import Lib
from time import sleep

class TestsPage(Lib):
    'Coloquem os localizadores dos elementos aqui, vai facilitar!'
    URL = 'https://undbclassroom.undb.edu.br'
    __LOGIN_DIRETO_URL = 'https://undbclassroom.undb.edu.br/login/index.php#'
    __EMAIL_TEXTBOX =  By.ID, 'username'
    __SENHA_TEXTBOX = By.ID, 'password'
    __ACESSAR_BUTTON = By.CLASS_NAME, 'btn-primary'
    __ESQUECEU_SENHA_BUTTON = By.XPATH, '//a[contains(text(), "Esqueceu o seu usuário ou senha?")]'
    __ID_USUARIO_TEXTBOX = By.ID, 'id_username'
    __BUSCAR_BUTTON = By.NAME, 'submitbuttonusername'
    __ID_EMAIL_TEXTBOX = By.ID, 'id_email'
    __ACESSAR_TEIA = By.XPATH, '//*[@id="page"]/div[2]/div/div/div[1]/div/a'
    __ACESSAR_PORTAL = By.XPATH, '//*[@id="page"]/div[2]/div/div/div[2]/div/a'
    __ACESSAR_SITE = By.XPATH, '//*[@id="page"]/div[2]/div/div/div[3]/div/a'
    __LEMBRAR_USUARIO = By.NAME, "rememberusername"
    __ACESSAR_LINK_PLAYSTORE = By.XPATH, '//*[@id="top-footer"]/div/div/div[1]/h4/a[1]/img'
    __CALENDARIO = By.XPATH, '//*[@id="nav-drawer"]/ul/li[3]/a'
    __SETA_CALENDARIO = By.CLASS_NAME, 'arrow_text'
    __ACESSAR_LINK_APPSTORE = By.XPATH, '//*[@id="top-footer"]/div/div/div[1]/h4/a[2]/img'
    __ACESSAR_EMAIL_INSTITUCIONAL = By.XPATH, '//*[@id="boxForm"]/div/div/div/a'
    __ACESSAR_BARRA_OPCOES = By.XPATH, '//*[@id="action-menu-toggle-1"]'
    __ACESSSAR_SAIR = By.XPATH, '//*[@id="action-menu-1-menu"]/a[7]'
    __EMAIL_GOOGLE = By.ID, 'identifierId'
    __BOTAO_PROXIMO = By.XPATH, '//*[@id="identifierNext"]/div/button'

    def __init__(self, driver):
        self.driver = driver
    
    def ct_0001(self, user, password):
        #Teste de login
        self.open_page(self.URL)
        self.fill(self.__EMAIL_TEXTBOX, user)
        self.fill(self.__SENHA_TEXTBOX, password)
        self.click(self.__ACESSAR_BUTTON)
        text = 'UNDB Classroom'
        assert text in self.driver.title
    
    def ct_0002(self, user):
        #Alteração de usuário ou senha pela identificação do usuário
        self.open_page(self.URL)
        self.click(self.__ESQUECEU_SENHA_BUTTON)
        self.fill(self.__ID_USUARIO_TEXTBOX, user)
        self.click(self.__BUSCAR_BUTTON)
        text = 'Se o usuário e o email estiverem corretos um email deve ter sido enviado a você.'
        assert text in self.driver.title

    def ct_0003(self, email):
        #Alteração de usuário ou senha pelo email institucional
        self.open_page(self.URL)
        self.click(self.__ESQUECEU_SENHA_BUTTON)
        self.fill(self.__ID_EMAIL_TEXTBOX, email)
        self.click(self.__BUSCAR_BUTTON)
        text = 'Se o usuário e o email estiverem corretos um email deve ter sido enviado a você.'
        assert text in self.driver.title
    
    def ct_0004(self,):...
    
    def ct_0005(self,):...
    
    def ct_0006(self,):...
    
    def ct_0007(self,):...
    
    def ct_0008(self,):...
    
    def ct_0009(self,):...
    
    def ct_0010(self,):...
    
    def ct_0011(self,):...

    def ct_0012(self,):...
    def ct_0013(self,):...
    def ct_0014(self,):...
    def ct_0015(self,):...
    def ct_0016(self,):...
    def ct_0017(self,):...
    def ct_0018(self,):...
    def ct_0019(self,):...
    def ct_0020(self,):...
    
    def ct_0021(self):
        #Redirecionamento do link do site TEIA
        self.open_page(self.URL)
        sleep(2)
        self.click(self.__ACESSAR_TEIA)
        text = 'Espaço Teia'
        assert text in self.driver.title

    def ct_0022(self,):
        #Redirecionamento do link do site do portal academico
        self.open_page(self.URL)
        sleep(2)
        self.click(self.__ACESSAR_PORTAL)
        text = 'Portal do Aluno'
        assert text in self.driver.title

    def ct_0023(self,):
        #Redirecionamento do link do site da UNDB
        self.open_page(self.URL)
        sleep(2)
        self.click(self.__ACESSAR_SITE)
        text = 'Sou UNDB'
        assert text in self.driver.title

    def ct_0024(self,email):
        #Testagem de e-mail institucional
        self.ct_0029()
        self.fill(self.__EMAIL_GOOGLE, email)
        result = self.driver.find_element(*self.__BOTAO_PROXIMO).is_enabled()
        assert result is True

    def ct_0025(self,):
        #Checagem de identificação de usuário
        self.open_page(self.__LOGIN_DIRETO_URL)
        self.click(self.__LEMBRAR_USUARIO)
        result = self.driver.find_element(*self.__LEMBRAR_USUARIO).is_selected()
        assert result is True

    def ct_0026(self,):
        #Redirecionamento do site da google play store
        self.open_page(self.URL)
        self.click(self.__ACESSAR_LINK_PLAYSTORE)
        text = 'UNDB Classroom'
        assert text in self.driver.title

    def ct_0027(self,):
        #Chave de eventos e visualização mensal
        self.ct_0001('user', 'password')
        self.click(self.__CALENDARIO)
        result = self.driver.find_element(*self.__SETA_CALENDARIO).is_enabled()
        assert result is True
        
    def ct_0028(self,):
        #Redirecionamento do site da app store
        self.open_page(self.URL)
        self.click(self.__ACESSAR_LINK_APPSTORE)
        text = 'UNDB Classroom'
        assert text in self.driver.title

    def ct_0029(self,):
        #Testagem de login com e-mail institucional
        self.open_page(self.URL)
        self.click(self.__ACESSAR_EMAIL_INSTITUCIONAL)
        text = 'Fazer login nas Contas do Google'
        assert text in self.driver.title

    def ct_0030(self,):
        #Testagem caixa de comando "sair"
        self.ct_0001('user', 'password')
        self.click(self.__ACESSAR_BARRA_OPCOES)
        self.click(self.__ACESSSAR_SAIR )
        text = 'UNDB Classroom'
        assert text in self.driver.title

    def ct_0031(self,):...
    def ct_0032(self,):...
    def ct_0033(self,):...
    def ct_0034(self,):...
    def ct_0035(self,):...
    def ct_0036(self,):...
    def ct_0037(self,):...
    def ct_0038(self,):...
    def ct_0039(self,):...
    def ct_0040(self,):...
    def ct_0041(self,):...
    def ct_0042(self,):...
    def ct_0043(self,):...
    def ct_0044(self,):...
    def ct_0045(self,):...
    def ct_0046(self,):...
    def ct_0047(self,):...
    def ct_0048(self,):...
    def ct_0049(self,):...
    def ct_0050(self,):...

    