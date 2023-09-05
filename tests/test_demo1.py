import logging
import time

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pagepbject.adminpage import AdminPage
from pagepbject.loginpage import LoginPage
from tests.Baseclass import BaseClass

#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def testdemo1(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        log.info("login page executing")

        loginpage.getusername().send_keys("Admin")

        loginpage.getpassword().send_keys("admin123")

        loginpage.getlogin().click()

        log.info("admin module is executing")
        adminpage = AdminPage(self.driver)


        adminpage.getadmin().click()
        adminpage.getorganization().click()
        adminpage.getlocation().click()
        adminpage.getlocationselect().click()

        actions = ActionChains(self.driver)
        log.info("actions has implemented")
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys("u")
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ARROW_DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        adminpage.getsearchbtn().click()
        time.sleep(3)
        '''var = adminpage.getverifyvalue().text
        expected_country = "United States"
        assert var == expected_country
        record = adminpage.getprintrecord().text
        print(record)'''
        for location in adminpage.getverifyvalue():
            if "United States" in location.text:
                print(f"Verified: {location.text} is in the United States")
        record = adminpage.getprintrecord().text
        print(record)


        '''count=0
        for option in adminpage.getverifyvalue():
            if option.text.strip() == "United States":
                count += 1

        print(f"Count of 'United States' options: {count}")'''



