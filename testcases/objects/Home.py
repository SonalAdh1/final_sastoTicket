import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from testcases.Config.config import TestData
from testcases.objects.utilities import utilities


# @pytest.mark.usefixtures("setup")
class Home(utilities):
    open_login = (By.XPATH, "//*[@data-target='#login-modal']")
    email = (By.ID, "login_username")
    password = (By.ID, "login_password")
    login = (By.ID, "btnLogin")
    login_err = (By.XPATH, "//*[class='alert alert-danger']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BaseUrl)
        self.driver.maximize_window()

    def openLogin(self):
        self.click(self.open_login)

    def fillLogin(self, useremail, userpassword):
        self.sendkeys(self.email, useremail)
        self.sendkeys(self.password, userpassword)
        self.click(self.login)

    # issue in getloginerr
    def getloginerr(self):
        try:
            loginerrmsg = self.gettext(self.login_err)
            print(loginerrmsg)
        except TimeoutException as e:
            print("Login Failed!!", e)



