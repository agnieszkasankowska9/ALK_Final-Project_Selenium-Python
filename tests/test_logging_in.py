from tests.base_test import BaseTest
from test_data.log_in_data import *
from time import sleep
import unittest

class RegistrationTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.authentication_page = self.home_page.click_sign_in()
        self.driver.implicitly_wait(15)

    @unittest.skip("Temporary skipping")
    def test_log_in(self):
        self.data = LogInData()
        self.driver.implicitly_wait(5)
        self.authentication_page.enter_existing_account_email(self.data.email)
        self.authentication_page.enter_existing_account_password(self.data.password)
        self.my_account_page = self.authentication_page.click_sign_in()
        self.driver.implicitly_wait(5)
        expected_url = "https://automationpractice.techwithjatin.com/my-account"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)
        print(f"Expected url: {expected_url}")
        print(f"Actual url: {actual_url}")




