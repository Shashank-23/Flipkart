import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def initialize_Browser_URL():
    browser_name = "chrome"
    URL="https://learn.letskodeit.com/p/practice"
    if browser_name == "chrome":
        driver = webdriver.Chrome("C:\\Users\\e01710\\PycharmProjects\\Flipkart\\Resources\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Chrome("C:\\Users\\e01710\\PycharmProjects\\Flipkart\\Resources\\chromedriver.exe")
    else:
        print("Browser not Supported")
        exit(0)

    driver.maximize_window()
    driver.get(URL)

    yield driver
    driver.quit()