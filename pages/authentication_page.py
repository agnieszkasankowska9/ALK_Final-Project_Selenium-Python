from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.my_account_page import MyAccountPage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


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
        self.wait.visible(Locators.EXISTING_ACCOUNT_EMAIL).send_keys(email)

    def enter_existing_account_password(self, password):
        """
        Enter existing user's password to log in
        """
        self.wait.visible(Locators.EXISTING_ACCOUNT_PASSWORD).send_keys(password)

    def click_sign_in(self):
        """
        Click Sign In button
        :return: MyAccountPage
        """
        self.wait.clickable(Locators.SIGN_IN_BUTTON).click()
        return MyAccountPage(self.driver)

    def _verify_page(self):
        self.wait.visible(Locators.SIGN_IN_BUTTON)