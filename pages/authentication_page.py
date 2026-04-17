from pages.base_page import BasePage
from selenium.webdriver.common.by import By
# from pages.create_account_page import CreateAccountPage

class Locators:
    """
    Authentication Page locators
    """
    EXISTING_ACCOUNT_EMAIL = (By.ID, 'email')
    EXISTING_ACCOUNT_PASSWORD = (By.ID, 'passwd')
    SIGN_IN_BUTTON = (By.ID, 'SubmitLogin')


class AuthenticationPage(BasePage):
    """
    Authentication Page Object
    """
    def enter_existing_account_email(self, email):
        """
        Enter existing user's email in order to log in
        """
        self.driver.find_element(*Locators.EXISTING_ACCOUNT_EMAIL).send_keys(email)

    def enter_existing_account_password(self, password):
        """
        Enter existing user's password to log in
        """
        self.driver.find_element(*Locators.EXISTING_ACCOUNT_PASSWORD).send_keys(password)

    def click_sign_in(self):
        """
        Click Sign In button
        :return: MyAccountPage
        """
        self.driver.find_element(*Locators.SIGN_IN_BUTTON).click()

        # return MyAccountPage(self.driver)