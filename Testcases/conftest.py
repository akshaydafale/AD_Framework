import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver=webdriver.Chrome()
    return driver

## always remember setup inherit in every test cases and after that --> driver =setup




