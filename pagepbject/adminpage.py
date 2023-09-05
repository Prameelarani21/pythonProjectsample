from select import select
from selenium.webdriver.common.by import By


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
    admin = (By.XPATH, "//span[text()='Admin']")
    organization = (By.XPATH, "//span[text()='Organization ']")
    location = (By.LINK_TEXT, "Locations")
    locationselect = (By.XPATH, "//i[contains(@class,'oxd-select-text--arrow')]")
    searchbtn = (By.XPATH, "//button[@type='submit']")
    #verifyvalue = (By.XPATH, "//div[text()='United States']")
    verifyvalue = (By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div")
    printrecord = (By.XPATH, "//span[text()=' (3) Records Found']")
    def getadmin(self):
        return self.driver.find_element(*AdminPage.admin)
    def getorganization(self):
        return self.driver.find_element(*AdminPage.organization)
    def getlocation(self):
        return self.driver.find_element(*AdminPage.location)
    def getlocationselect(self):
        return self.driver.find_element(*AdminPage.locationselect)

    #def getunitedstates(self):
        #return self.driver.find_element(*AdminPage.unitedstates)

    def getsearchbtn(self):
        return self.driver.find_element(*AdminPage.searchbtn)

    def getverifyvalue(self):
        return self.driver.find_elements(*AdminPage.verifyvalue)


    def getprintrecord(self):
        return self.driver.find_element(*AdminPage.printrecord)









