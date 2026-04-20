from selenium.webdriver.support.select import Select
from pages.addresses_page import AddressesPage
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
    NUMBER_VISIBLE_ERRORS = (By.XPATH, '//div[@class="alert alert-danger"]/p')
    VISIBLE_ERRORS = (By.XPATH, '//div[@class="alert alert-danger"]/ol/li')
    INFO_TITLE = (By.XPATH, '//*[@class="info-title"]')
    ACCOUNT_NAME = (By.XPATH, '//*[@title="View my customer account"]/span')



class AddressPage(BasePage):
    """
    Address Page objects
    """
    def enter_new_first_name(self, first_name):
        """
        Change visible first name to another first name
        """
        self.wait.visible(Locators.FIRST_NAME).clear()
        self.wait.visible(Locators.FIRST_NAME).send_keys(first_name)

    def enter_new_last_name(self, last_name):
        """
        Change visible last name to another last name
        """
        self.wait.visible(Locators.LAST_NAME).clear()
        self.wait.visible(Locators.LAST_NAME).send_keys(last_name)

    def enter_company(self, company):
        """
        Enter Company
        """
        self.wait.visible(Locators.COMPANY).send_keys(company)

    def enter_address(self, address):
        """
        Enter Address - line 1
        """
        self.wait.visible(Locators.ADDRESS).send_keys(address)

    def enter_address_line_2(self, address2):
        """
        Enter Address - line 2
        """
        self.wait.visible(Locators.ADDRESS_LINE_2).send_keys(address2)

    def enter_city(self, city):
        """
        Enter City
        """
        self.wait.visible(Locators.CITY).send_keys(city)

    def enter_home_phone(self, home_phone):
        """
        Enter Home phone
        """
        self.wait.visible(Locators.HOME_PHONE).send_keys(home_phone)

    def enter_mobile_phone(self, mobile_phone):
        """
        Enter Mobile phone
        """
        self.wait.visible(Locators.MOBILE_PHONE).send_keys(mobile_phone)

    def enter_additional_information(self, additional_information):
        """
        Enter Additional information
        """
        self.wait.visible(Locators.ADDITIONAL_INFORMATION).send_keys(additional_information)

    def enter_new_address_tile(self, address_tile):
        """
        Remove a default "My address" title and enter a new one.
        """
        self.wait.visible(Locators.ADDRESS_TITLE).clear()
        self.wait.visible(Locators.ADDRESS_TITLE).send_keys(address_tile)

    def enter_zip_post_code(self, post_code):
        """
        Enter Zip/Postal Code
        """
        self.wait.visible(Locators.ZIP_POSTAL_CODE).send_keys(post_code)

    def select_state(self, state):
        """
        Select State
        """
        dropdown = Select(self.driver.find_element(*Locators.STATE_SELECT))
        dropdown.select_by_visible_text(state)

    def select_country(self, country):
        """
        Select Country
        """
        dropdown = Select(self.driver.find_element(*Locators.COUNTRY_SELECT))
        dropdown.select_by_visible_text(country)

    def click_save_button(self):
        self.driver.find_element(*Locators.SAVE_BUTTON).click()

        try:
            self.get_number_of_errors_message()
            return self
        except:
            return AddressesPage(self.driver)

    def get_account_name(self):
        """
        Get visible account name = First name + Last name
        """
        return self.wait.visible(Locators.ACCOUNT_NAME).text

    def get_entered_first_name(self):
        """
        Get first name entered during registration
        """
        return self.wait.visible(Locators.FIRST_NAME).get_attribute("value")

    def get_entered_last_name(self):
        """
        Get last name entered during registration
        """
        return self.wait.visible(Locators.LAST_NAME).get_attribute("value")

    def get_address_tile(self):
        """
        Get address title.
        """
        return self.wait.visible(Locators.ADDRESS_TITLE).get_attribute("value")

    def get_number_of_errors_message(self):
        """
        Get Number of Errors message
        """
        return self.wait.visible(Locators.NUMBER_VISIBLE_ERRORS).text

    def get_visible_errors(self):
        """
        Return visible errors
        """
        all_errors = self.driver.find_elements(*Locators.VISIBLE_ERRORS)
        visible_errors = []
        for error in all_errors:
            visible_errors.append(error.text)
        return visible_errors

    def _verify_page(self):
        assert "To add a new address" in self.wait.visible(Locators.INFO_TITLE).text

