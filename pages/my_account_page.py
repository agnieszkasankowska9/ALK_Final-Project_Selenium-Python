from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    """
    MyAccount Page locators
    """
    ADD_MY_FIRST_ADDRESS_BUTTON = (By.XPATH, '//*[@title="Add my first address"]')


class MyAccountPage(BasePage):
    """
    MyAccount Page Object
    """
    def click_add_my_first_address(self):
        """
        Click Add my first address button
        :return: Address Page object
        """
        self.driver.find_element(*Locators.ADD_MY_FIRST_ADDRESS_BUTTON).click()
        # return AddressPage (self, driver)