from selenium import webdriver
import pytest


@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver

    yield
    # code written after yield is taken as teardown
    web_driver.close()

