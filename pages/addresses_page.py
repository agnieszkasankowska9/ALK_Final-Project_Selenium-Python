from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators:
    """
    Addresses Page elements Locators
    """
    ADDED_ADDRESS_TITLE = (By.XPATH, '//*[@class="page-subheading"]')
    ADDED_COMPANY = (By.XPATH, '//*[@class="address_company"]')
    ADDED_ADDRESS = (By.XPATH, '//*[@class="address_address1"]')
    ADDED_ADDRESS_LINE_2 = (By.XPATH, '//*[@class="address_address2"]')
    ADDED_CITY = (By.XPATH, '//*[@class="last_item item box"]/li[5]/span[1]')
    ADDED_STATE = (By.XPATH, '//*[@class="last_item item box"]/li[5]/span[2]')
    ADDED_ZIP_POSTAL_CODE = (By.XPATH, '//*[@class="last_item item box"]/li[5]/span[3]')
    ADDED_COUNTRY = (By.XPATH, '//*[@class="last_item item box"]/li[6]/span')
    ADDED_HOME_PHONE = (By.XPATH,'//*[@class="last_item item box"]/li[7]/span')
    ADDED_MOBILE_PHONE = (By.XPATH, '//*[@class="last_item item box"]/li[8]/span')
    DELETE_BUTTON = (By.XPATH, '//*[@title="Delete"]')
    BACK_TO_YOUR_ACCOUNT = (By.XPATH, '//*[@id="center_column"]/ul/li[1]/a')


class AddressesPage(BasePage):
    """
    Addresses Page objects
    """

    def delete_first_address(self):
        """
        Delete first address: Click "Delete" button, accept alert.
        """
        self.driver.find_element(*Locators.DELETE_BUTTON).click()
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert.accept()

    def get_added_address_tile(self):
        """
        Get added address title
        """
        return self.wait.visible(Locators.ADDED_ADDRESS_TITLE).text

    def get_added_company(self):
        """
        Get added company
        """
        return self.wait.visible(Locators.ADDED_COMPANY).text

    def get_added_address(self):
        """
        Get added address
        """
        return self.wait.visible(Locators.ADDED_ADDRESS).text

    def get_added_address_line_2(self):
        """
        Get added address (line 2)
        """
        return self.wait.visible(Locators.ADDED_ADDRESS_LINE_2).text

    def get_added_city(self):
        """
        Get added City
        """
        return self.wait.visible(Locators.ADDED_CITY).text

    def get_added_state(self):
        """
        Get added State
        """
        return self.wait.visible(Locators.ADDED_STATE).text

    def get_added_zip_postal_code(self):
        """
        Get added Zip/Postal Code
        """
        return self.wait.visible(Locators.ADDED_ZIP_POSTAL_CODE).text

    def get_added_country(self):
        """
        Get added Country
        """
        return self.wait.visible(Locators.ADDED_COUNTRY).text

    def get_added_home_phone(self):
        """
        Get added home phone
        """
        return self.wait.visible(Locators.ADDED_HOME_PHONE).text

    def get_added_mobile_phone(self):
        """
        Get added mobile phone
        """
        return self.wait.visible(Locators.ADDED_MOBILE_PHONE).text

    def go_back_to_my_account(self):
        """
        Going back to My account page
        """
        from pages.my_account_page import MyAccountPage
        self.wait.clickable(Locators.BACK_TO_YOUR_ACCOUNT).click()
        return MyAccountPage (self.driver)

    def is_delete_button_visible(self):
        """
        Check if Delete button next to First added address is visible
        """
        return len(self.driver.find_elements(*Locators.DELETE_BUTTON)) > 0
