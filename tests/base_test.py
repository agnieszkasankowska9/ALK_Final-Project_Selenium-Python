from pages.home_page import HomePage
from selenium import webdriver
import unittest

class BaseTest(unittest.TestCase):
    """
    Base Test for every Test Case
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/")
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()
