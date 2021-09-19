from lib import Lib
from tests_page import TestsPage
from time import sleep

lib = Lib()
website = 'https://undbclassroom.undb.edu.br'

driver = lib.start_browser()

undb_classroom = TestsPage(driver)
undb_classroom.open_page(website)
undb_classroom.ct_001('seu usuário', 'sua senha')

assert 'UNDB' in driver.title

print('')