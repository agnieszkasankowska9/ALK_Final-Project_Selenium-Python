from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Locators:
    """
    Address Page elements Locators
    """
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    COMPANY = (By.ID, "company")
    ADDRESS = (By.ID, "address1")
    ADDRESS_LINE_2 = (By.ID, "address2")
    CITY = (By.ID, "city")
    STATE_SELECT = (By.ID, "id_state")
    ZIP_POSTAL_CODE = (By.ID, "postcode")
    COUNTRY_SELECT = (By.ID, "id_country")
    HOME_PHONE = (By.ID, "phone")
    MOBILE_PHONE = (By.ID, "phone_mobile")
    ADDITIONAL_INFORMATION = (By.ID, "other")
    ADDRESS_TITLE = (By.ID, "alias")
    SAVE_BUTTON = (By.ID, "submitAddress")

class AddressPage(BasePage):
    """
    Address Page objects
    """

    def get_entered_first_name(self):
        """
        Get first name entered during registration
        """
        return self.driver.find_element(*Locators.FIRST_NAME).get_attribute("value")

    def get_entered_last_name(self):
        """
        Get last name entered during registration
        """
        return self.driver.find_element(*Locators.LAST_NAME).get_attribute("value")

    def enter_company(self, company):
        """
        Enter Company
        """
        self.driver.find_element(*Locators.COMPANY).send_keys(company)

    def enter_address(self, address):
        """
        Enter Address - line 1
        """
        self.driver.find_element(*Locators.ADDRESS).send_keys(address)

    def enter_address_line_2(self, address2):
        """
        Enter Address - line 2
        """
        self.driver.find_element(*Locators.ADDRESS_LINE_2).send_keys(address2)

    def enter_city(self, city):
        """
        Enter City
        """
        self.driver.find_element(*Locators.CITY).send_keys(city)

    def select_state(self, state):
        """
        Select State
        """
        state = Select(self.driver.find_element(*Locators.STATE_SELECT))
        state.select_by_value(str(state))

    def select_country(self, state):
        """
        Select Country
        """
        country = Select(self.driver.find_element(*Locators.COUNTRY_SELECT))
        country.select_by_value(str(country))

    def enter_home_phone(self, home_phone):
        """
        Enter Home phone
        """
        self.driver.find_element(*Locators.HOME_PHONE).send_keys(home_phone)

    def enter_mobile_phone(self, mobile_phone):
        """
        Enter Mobile phone
        """
        self.driver.find_element(*Locators.MOBILE_PHONE).send_keys(mobile_phone)

    def enter_additional_information(self, additional_information):
        """
        Enter Additional information
        """
        self.driver.find_element(*Locators.ADDITIONAL_INFORMATION).send_keys(additional_information)

    def get_address_tile(self):
        """
        "My address" is added as default address title.
        """
        return self.driver.find_element(*Locators.ADDRESS_TITLE).get_attribute("value")

    def enter_new_address_tile(self, address_tile):
        """
        Remove a default "My address" title and enter a new one.
        """
        self.driver.find_element(*Locators.ADDRESS_TITLE).clear()
        self.driver.find_element(*Locators.ADDRESS_TITLE).send_keys(address_tile)




