import pytest

from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(2)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    print("test ended")
    driver.close()
