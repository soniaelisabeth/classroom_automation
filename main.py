from lib import Lib
from tests_page import TestsPage
from time import sleep

lib = Lib()
driver = lib.start_browser()
undb_classroom = TestsPage(driver)

# undb_classroom.ct_001('seu usuário', 'sua senha')
# undb_classroom.ct_002('usuario')
# undb_classroom.ct_003('email@institucional.com')

undb_classroom.ct_0024('andrekroliveira@gmail.com')

# assert 'UNDB' in driver.title

print('')