from lib import Lib
from tests_page import TestsPage
from time import sleep

lib = Lib()
driver = lib.start_browser()

undb_classroom = TestsPage(driver)
undb_classroom.ct_001('seu usuário', 'sua senha')

assert 'UNDB' in driver.title

print('')