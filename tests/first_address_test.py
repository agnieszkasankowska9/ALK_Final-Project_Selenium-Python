from tests.base_test import BaseTest
from test_data.log_in_data import *
import test_data.first_address_data
from ddt import ddt, data, unpack
from time import sleep
import unittest


@ddt
class FirstAddressTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.data = LogInData()
        self.authentication_page = self.home_page.click_sign_in()
        self.authentication_page.enter_existing_account_email(self.data.email)
        self.authentication_page.enter_existing_account_password(self.data.password)
        self.my_account_page = self.authentication_page.click_sign_in()
        self.driver.implicitly_wait(5)
        self.my_address_page = self.my_account_page.click_add_my_first_address()
        self.driver.implicitly_wait(5)

    @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_no_city.csv"))
    @unpack
    def testNoCity(self, testcaseid, firstname, lastname, company, address, address2, city, state, postalcode, country, homephone, mobilephone, additionalinfo, addresstitle):
        self.assertEqual(self.data.firstname, self.my_address_page.get_entered_first_name())
        self.assertEqual(self.data.lastname, self.my_address_page.get_entered_last_name())
        self.my_address_page.enter_address(address)
        self.my_address_page.select_state(state)
        self.my_address_page.enter_zip_post_code(postalcode)
        self.my_address_page.select_country(country)
        self.my_address_page.enter_home_phone(homephone)
        self.my_address_page.click_save_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.my_address_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.my_address_page.get_visible_errors()
        expected_errors = ["city is required."]
        self.assertCountEqual(expected_errors, visible_errors)

    @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_phone_negative.csv"))
    @unpack
    def testPhone(self, testcaseid, firstname, lastname, company, address, address2, city, state, postalcode, country, homephone, mobilephone, additionalinfo, addresstitle, expectederrors):
        self.assertEqual(self.data.firstname, self.my_address_page.get_entered_first_name())
        self.assertEqual(self.data.lastname, self.my_address_page.get_entered_last_name())
        self.my_address_page.enter_address(address)
        self.my_address_page.enter_city(city)
        self.my_address_page.select_state(state)
        self.my_address_page.enter_zip_post_code(postalcode)
        self.my_address_page.select_country(country)
        self.my_address_page.enter_home_phone(homephone)
        self.my_address_page.enter_mobile_phone(mobilephone)
        self.my_address_page.click_save_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.my_address_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.my_address_page.get_visible_errors()
        self.assertIn(expectederrors, visible_errors)


    @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_data_all.csv"))
    @unpack
    def testNoState(self, testcaseid, firstname, lastname, company, address, address2, city, state, postalcode, country, homephone, mobilephone, additionalinfo, addresstitle):
        self.assertEqual(self.data.firstname, self.my_address_page.get_entered_first_name())
        self.assertEqual(self.data.lastname, self.my_address_page.get_entered_last_name())
        self.my_address_page.enter_address(address)
        self.my_address_page.enter_city(city)
        self.my_address_page.enter_zip_post_code(postalcode)
        self.my_address_page.select_country(country)
        self.my_address_page.enter_home_phone(homephone)
        self.my_address_page.click_save_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.my_address_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.my_address_page.get_visible_errors()
        expected_errors = ["This country requires you to chose a State."]
        self.assertCountEqual(expected_errors, visible_errors)
        sleep(1)

    # @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_zip_postal_code_negative.csv"))
    @unpack
    def testZipPostalCode(self, testcaseid, firstname, lastname, company, address, address2, city, state, postalcode, country,
                    homephone, mobilephone, additionalinfo, addresstitle):
        self.assertEqual(self.data.firstname, self.my_address_page.get_entered_first_name())
        self.assertEqual(self.data.lastname, self.my_address_page.get_entered_last_name())
        self.my_address_page.enter_address(address)
        self.my_address_page.enter_city(city)
        self.my_address_page.select_state(state)
        self.my_address_page.enter_zip_post_code(postalcode)
        self.my_address_page.select_country(country)
        self.my_address_page.enter_home_phone(homephone)
        self.my_address_page.click_save_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.my_address_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.my_address_page.get_visible_errors()
        expected_errors = ["The Zip/Postal code you've entered is invalid. It must follow this format: 00000"]
        self.assertCountEqual(expected_errors, visible_errors)
        sleep(3)