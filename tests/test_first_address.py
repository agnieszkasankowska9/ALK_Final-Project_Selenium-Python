from selenium.webdriver.support.wait import WebDriverWait
from tests.base_test import BaseTest
from test_data.log_in_data import *
import test_data.first_address_data
from ddt import ddt, data, unpack
import HtmlTestRunner
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
        if not self.my_account_page.is_add_my_first_address_visible():
            self.my_addresses_page = self.my_account_page.click_my_addresses()
            self.my_addresses_page.delete_first_address()
            self.my_account_page = self.my_addresses_page.go_back_to_my_account()
        self.address_page = self.my_account_page.click_add_my_first_address()



    # @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_city_negative.csv"))
    @unpack
    def testNoCity(self, testcaseid, testcasename, firstname, lastname, company, address, address2, city, state, postalcode, country, homephone, mobilephone, additionalinfo, addresstitle):
        self._testMethodName = f"{testcaseid}_{testcasename}"
        self.address_page.enter_address(address)
        self.address_page.select_state(state)
        self.address_page.enter_zip_post_code(postalcode)
        self.address_page.select_country(country)
        self.address_page.enter_home_phone(homephone)
        self.address_page.click_save_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.address_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.address_page.get_visible_errors()
        expected_errors = ["city is required."]
        self.assertCountEqual(expected_errors, visible_errors)

    # @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_phone_negative.csv"))
    @unpack
    def testPhone(self, testcaseid, testcasename, firstname, lastname, company, address, address2, city, state, postalcode, country, homephone, mobilephone, additionalinfo, addresstitle, expectederrors):
        self._testMethodName = f"{testcaseid}_{testcasename}"
        self.address_page.enter_address(address)
        self.address_page.enter_city(city)
        self.address_page.select_state(state)
        self.address_page.enter_zip_post_code(postalcode)
        self.address_page.select_country(country)
        self.address_page.enter_home_phone(homephone)
        self.address_page.enter_mobile_phone(mobilephone)
        self.address_page.click_save_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.address_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.address_page.get_visible_errors()
        self.assertIn(expectederrors, visible_errors)

    # @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_state_negative.csv"))
    @unpack
    def testNoState(self, testcaseid, testcasename, firstname, lastname, company, address, address2, city, state, postalcode, country, homephone, mobilephone, additionalinfo, addresstitle):
        self._testMethodName = f"{testcaseid}_{testcasename}"
        self.address_page.enter_address(address)
        self.address_page.enter_city(city)
        self.address_page.enter_zip_post_code(postalcode)
        self.address_page.select_country(country)
        self.address_page.enter_home_phone(homephone)
        self.address_page.click_save_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.address_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.address_page.get_visible_errors()
        expected_errors = ["This country requires you to chose a State."]
        self.assertCountEqual(expected_errors, visible_errors)

    # @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_zip_postal_code_negative.csv"))
    @unpack
    def testZipPostalCode(self, testcaseid, testcasename, firstname, lastname, company, address, address2, city, state, postalcode, country, homephone, mobilephone, additionalinfo, addresstitle):
        self._testMethodName = f"{testcaseid}_{testcasename}"
        self.address_page.enter_address(address)
        self.address_page.enter_city(city)
        self.address_page.select_state(state)
        self.address_page.enter_zip_post_code(postalcode)
        self.address_page.select_country(country)
        self.address_page.enter_home_phone(homephone)
        self.address_page.click_save_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.address_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.address_page.get_visible_errors()
        expected_errors = ["The Zip/Postal code you've entered is invalid. It must follow this format: 00000"]
        self.assertCountEqual(expected_errors, visible_errors)

    # @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_first_name_negative.csv"))
    @unpack
    def testFirstName(self, testcaseid, testcasename, firstname, lastname, company, address, address2, city, state, postalcode, country, homephone, mobilephone, additionalinfo, addresstitle, expectederrors):
        self._testMethodName = f"{testcaseid}_{testcasename}"
        self.address_page.enter_new_first_name(firstname)
        self.address_page.enter_address(address)
        self.address_page.enter_city(city)
        self.address_page.select_state(state)
        self.address_page.enter_zip_post_code(postalcode)
        self.address_page.select_country(country)
        self.address_page.enter_home_phone(homephone)
        self.address_page.click_save_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.address_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.address_page.get_visible_errors()
        self.assertIn(expectederrors, visible_errors)

    # @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_last_name_negative.csv"))
    @unpack
    def testLastName(self, testcaseid, testcasename, firstname, lastname, company, address, address2, city, state, postalcode, country, homephone, mobilephone, additionalinfo, addresstitle, expectederrors):
        self._testMethodName = f"{testcaseid}_{testcasename}"
        self.address_page.enter_new_last_name(lastname)
        self.address_page.enter_address(address)
        self.address_page.enter_city(city)
        self.address_page.select_state(state)
        self.address_page.enter_zip_post_code(postalcode)
        self.address_page.select_country(country)
        self.address_page.enter_home_phone(homephone)
        self.address_page.click_save_button()
        expected_number_of_errors_message = "There is 1 error"
        actual_number_of_errors_message = self.address_page.get_number_of_errors_message()
        self.assertEqual(expected_number_of_errors_message, actual_number_of_errors_message)
        visible_errors = self.address_page.get_visible_errors()
        self.assertIn(expectederrors, visible_errors)

    # @unittest.skip("Temporary skipping")
    @data(*test_data.first_address_data.get_csv_data("test_data/first_address_data_positive.csv"))
    @unpack
    def test_add_address_success(self, testcaseid, testcasename, firstname, lastname, company, address, address2, city, state, postalcode, country, homephone, mobilephone, additionalinfo, addresstitle):
        self._testMethodName = f"{testcaseid}_{testcasename}"
        self.address_page.enter_company(company)
        self.address_page.enter_address(address)
        self.address_page.enter_address_line_2(address2)
        self.address_page.enter_city(city)
        self.address_page.select_state(state)
        self.address_page.enter_zip_post_code(postalcode)
        self.address_page.select_country(country)
        self.address_page.enter_home_phone(homephone)
        self.address_page.enter_mobile_phone(mobilephone)
        self.address_page.enter_additional_information(additionalinfo)
        self.address_page.enter_new_address_tile(addresstitle)
        self.my_addresses_page = self.address_page.click_save_button()
        WebDriverWait(self.driver, 10).until(
            lambda d: d.current_url == "https://automationpractice.techwithjatin.com/addresses")
        expected_url = "https://automationpractice.techwithjatin.com/addresses"
        actual_url = self.driver.current_url
        full_name = self.my_addresses_page.get_added_first_name() + " " + self.my_addresses_page.get_added_last_name()
        self.assertEqual(full_name, self.my_addresses_page.get_account_name())
        self.assertEqual(expected_url, actual_url)
        self.assertEqual(addresstitle.upper(), self.my_addresses_page.get_added_address_tile())
        self.assertEqual(company, self.my_addresses_page.get_added_company())
        self.assertEqual(address, self.my_addresses_page.get_added_address())
        self.assertEqual(address2, self.my_addresses_page.get_added_address_line_2())
        self.assertEqual(city+",", self.my_addresses_page.get_added_city())
        self.assertEqual(state, self.my_addresses_page.get_added_state())
        self.assertEqual(postalcode, self.my_addresses_page.get_added_zip_postal_code())
        self.assertEqual(country, self.my_addresses_page.get_added_country())
        self.assertEqual(homephone, self.my_addresses_page.get_added_home_phone())
        self.assertEqual(mobilephone, self.my_addresses_page.get_added_mobile_phone())


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))