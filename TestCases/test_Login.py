from Pages.login_page import LoginPage
from selenium import webdriver
import unittest
import pytest

@pytest.mark.usefixtures("initialize_Browser_URL")
class Login(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,initialize_Browser_URL):
        self.lp = LoginPage(self.driver)

    def test_valid_login(self):
        self.lp.login("test@email.com","abcabc")

    def test_Invalid_login(self):
        self.lp.login("test@email.com","abcabvsdc")


