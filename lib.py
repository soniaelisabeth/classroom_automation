from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class Lib():
    '''
    Para não precisar ficarmos repetindo código, criei métodos simples
    que já fazem o que precisamos.
    Se quiserem acessar o driver pela test_page para adicionar mais algum método
    do selenium basta chamar, por exemplo: self.driver.set_focus()
    '''
    WEBDRIVER_PATH = '.\\tools\\chromedriver.exe'

    def start_browser(self):
        self.driver = webdriver.Chrome(self.WEBDRIVER_PATH)
        return self.driver
    
    def open_page(self, url):
        self.driver.maximize_window()
        self.driver.get(url)

    def click(self, locator):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator)).click()
    
    def fill(self, locator, text):
        elem = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)
    
    def hover_to_element(self, locator):
        element_to_hover_over = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
