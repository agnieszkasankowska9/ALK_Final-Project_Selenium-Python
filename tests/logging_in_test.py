from tests.base_test import BaseTest
from time import sleep
from test_data.log_in_data import *

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.authentication_page = self.home_page.click_sign_in()
        sleep(2)


    def test_log_in(self):
        self.data = LogInData()
        sleep(2)
        self.authentication_page.enter_existing_account_email(self.data.email)
        self.authentication_page.enter_existing_account_password(self.data.password)
        self.my_account_page = self.authentication_page.click_sign_in()
        sleep(6)


