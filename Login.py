from time import sleep
import selenium.common.exceptions as se

from Armis import SLEEP


class Login:
    def __init__(self, test):
        self.browser = test.browser
        self.user = test.user
        self.password = test.password
        self.user_field = None
        self.pass_field = None
        self.navigate()
        self.retrieve_fields()

    def retrieve_fields(self):
        """
        Sets login text fields
        """
        self.user_field = self.browser.find_element_by_id('id_login')
        self.pass_field = self.browser.find_element_by_id('id_password')

    def navigate(self):
        """
        Goes to Login page
        """
        self.browser.find_element_by_link_text('Login').click()
        sleep(SLEEP)

    def test_bad_user(self):
        """
        Negative test - trying to log in with an invalid username
        """
        self.login(username=self.user[:-1])
        sleep(SLEEP)
        try:
            self.browser.find_element_by_class_name('nonfield')
        except se.NoSuchElementException:
            raise AssertionError('No error message found when trying to log with a bad USERNAME')

    def test_bad_pass(self):
        """
        Negative test - trying to log in with an invalid username
        """
        self.login(password=str(self.password[:-1]))
        sleep(SLEEP)
        try:
            self.browser.find_element_by_class_name('nonfield')
        except se.NoSuchElementException:
            raise AssertionError('No error message found when trying to log with a bad PASSWORD')

    def login(self, username='', password=''):
        """
        When in login page - Inserts username, password and submits
        """
        if not username:
            username = self.user
        if not password:
            password = self.password
        self.retrieve_fields()
        # Inserts username
        self.user_field.clear()
        self.user_field.send_keys(username)
        # Inserts password
        self.pass_field.clear()
        self.pass_field.send_keys(password)

        self.pass_field.submit()
