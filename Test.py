from selenium.webdriver import Chrome

from Playlists import Playlists
from Login import Login


class Test:
    def __init__(self, page, user, password):
        self.browser = Chrome(executable_path='C:\Python27\selenium\webdriver\chrome\chromedriver')
        self.browser.get(page)
        self.user = user
        self.password = password

    def test_login(self):
        log_test = Login(self)
        log_test.test_bad_user()
        log_test.test_bad_pass()
        log_test.login()

    def test_playlists(self):
        pl_test = Playlists(self)
        pl_test.test_add_pl()
