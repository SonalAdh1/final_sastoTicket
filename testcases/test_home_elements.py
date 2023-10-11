import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomeElements:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sastotickets.com/")
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def openLoginPage(self):
        self.driver.find_element(By.XPATH, "//*[@data-target='#login-modal']").click()

    def loginForm(self):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login_username")))
        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "login_password")))
        username_input.send_keys("sonal")
        password_input.send_keys("sonal")

    def clickLogin(self):
        login_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "btnLogin")))
        login_click.click()

    def closeLoginPage(self):
        login_close = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@data-dismiss='modal']")))
        login_close.click()

