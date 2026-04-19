class BasePage:
    """
    Base Page Object for each page
    """
    def __init__(self, driver):
        self.driver = driver
        from utils.wait_helper import WaitHelper
        self.wait = WaitHelper(driver)
        self._verify_page()

    def _verify_page(self):
        # site autotest
        pass