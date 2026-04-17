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
    STATE = (By.ID, "id_state")
    ZIP_POSTAL_CODE = (By.ID, "postcode")
    COUNTRY = (By.ID, "id_country")
    HOME_PHONE = (By.ID, "phone")
    MOBILE_PHONE = (By.ID, "phone_mobile")
    ADDITIONAL_INFORMATION = (By.ID, "other")
    ADDRESS_TITLE = (By.ID, "alias")
    SAVE_BUTTON = (By.ID, "submitAddress")








class AddressPage(BasePage):
    """
    Address Page Object
    """
    def xxx(self):
        """
        xxx
        """
