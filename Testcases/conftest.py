import pytest
from selenium import webdriver

# cross browser without changing code

def pytest_addoption(parser):  # pytest_addoption is a hook provided by pytest framework
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup():
    if browser=='chrome':
        driver=webdriver.Chrome()
        print('Launching Chrome browser ')

    elif browser=='firefox':
        driver=webdriver.Firefox()
        print('Launching Firefox browser ')

    elif browser=='edge':
        driver=webdriver.Edge()
        print('Launching Edge browser ')

    else:
        # for headless we have to write 3 line code
        from selenium.webdriver.common.service import Service
        # headless_option = webdriver.ChromeOptions()
        # headless_option.add_argument("headless")
        # driver=webdriver.Chrome(options= headless_option)
        # print('Launching Chrome browser ')
        driver=webdriver.Chrome()
        print('Launching Chrome browser ')

    driver.get('https://admin-demo.nopcommerce.com')
    return driver

## always remember setup inherit in every test cases and after that --> driver =setup




