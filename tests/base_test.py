from pages.home_page import HomePage
from selenium import webdriver
from pages.addresses_page import AddressesPage
import unittest
from time import sleep

class BaseTest(unittest.TestCase):
    """
    Base Test for every Test Case
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://automationpractice.techwithjatin.com/")
        self.home_page = HomePage(self.driver)


    def tearDown(self):
        self.driver.quit()

