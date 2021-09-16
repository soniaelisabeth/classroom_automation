from lib import Lib
from login_page import LoginPage
from time import sleep

lib = Lib()
undb_classroom = 'https://undbclassroom.undb.edu.br'

driver = lib.start_browser()

login_page = LoginPage(driver)
login_page.open_page(undb_classroom)

assert 'UNDB' in driver.title

print('')