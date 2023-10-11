import pytest
from selenium.webdriver.common.by import By

from testcases.Config.config import TestData
from testcases.testScenarios.test_base import BaseTest
from testcases.objects.Home import Home


# @pytest.mark.usefixtures("init_driver")
class Test_home(BaseTest):

    def test_openLoginPage(self):
        self.home = Home(self.driver)
        self.home.openLogin()
        self.home.fillLogin(TestData.User_email, TestData.User_password)
        self.home.getloginerr()



