from selenium.webdriver.support.wait import WebDriverWait
from pages.authentication_page import AuthenticationPage
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class Locators:
    """
    Home Page elements Locators
    """
    SIGN_IN_LINK = (By.CLASS_NAME, "login")

class HomePage(BasePage):
    """
    Home Page Object
    """

    def click_sign_in(self):
        """
        Click sign in and goes to Authentication_Page
        :return: Authentication_Page object
        """
        self.wait.clickable(Locators.SIGN_IN_LINK).click()
        return AuthenticationPage(self.driver)

    def _verify_page(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.title.startswith("Automation Practice"))