from selenium import webdriver
from selenium.webdriver import *
from datetime import date
import os
import undetected_chromedriver as uc


class pantryTest:
    """This test adds an item to the pantry page"""

    def __init__(self):
        self.driver = uc.Chrome()


    def to_pantry(self):
        """Navigate to pantry site"""

        self.driver.get('http://todoteamname-env.eba-entjj2xt.us-west-2.elasticbeanstalk.com/pantry')
        self.driver.maximize_window()


    def add_item(self, item_name):
        """Finds the name and expiration boxes and adds the passed in item name and todays date"""

        name_box = self.driver.find_element_by_name("name")
        expiration_box = self.driver.find_element_by_name("expiration")
        today = date.today()
        name_box.send_keys(item_name)
        expiration_box.send_keys(str(today))

        # Submits the item
        submit_button = self.driver.find_element_by_xpath("/html/body/div/form/input[4]")
        submit_button.click()


if __name__ == '__main__':
    pt = pantryTest()
    pt.to_pantry()

    #Currently we add 10 items to the list
    for i in range(10):
        pt.add_item("Test Item " + str(i))
