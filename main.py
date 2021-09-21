from lib import Lib
from tests_page import TestsPage
from time import sleep

lib = Lib()
driver = lib.start_browser()
undb_classroom = TestsPage(driver)

undb_classroom.ct_0010()
print('')