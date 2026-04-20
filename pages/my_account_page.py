from pages.addresses_page import AddressesPage
from selenium.webdriver.common.by import By
from pages.address_page import AddressPage
from pages.base_page import BasePage


class Locators:
    """
    MyAccount Page locators
    """
    ADD_MY_FIRST_ADDRESS_BUTTON = (By.XPATH, '//*[@title="Add my first address"]')
    MY_ADDRESSES_BUTTON = (By.XPATH, '//*[@title="Addresses"]')
    INFO_ACCOUNT = (By.XPATH, '//*[@class="info-account"]')


class MyAccountPage(BasePage):
    """
    MyAccount Page Object
    """

    def click_add_my_first_address(self):
        """
        Click Add my first address button
        :return: Address Page object
        """
        self.wait.clickable(Locators.ADD_MY_FIRST_ADDRESS_BUTTON).click()
        return AddressPage(self.driver)

    def is_add_my_first_address_visible(self):
        """
        Check if "Add my first address" button is visible
        """
        return len(self.driver.find_elements(*Locators.ADD_MY_FIRST_ADDRESS_BUTTON)) > 0

    def click_my_addresses(self):
        """
        Click My Addresses button
        :return: My addresses Page object
        """
        self.wait.clickable(Locators.MY_ADDRESSES_BUTTON).click()
        return AddressesPage (self.driver)

    def _verify_page(self):
        self.wait.visible(Locators.INFO_ACCOUNT)

