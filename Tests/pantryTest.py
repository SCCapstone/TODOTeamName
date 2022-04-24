from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
import os
from time import sleep
import undetected_chromedriver as uc


class pantryTest:
    """This test adds an item to the pantry page"""

    def __init__(self):
        self.driver = uc.Chrome()
        self.action = ActionChains(self.driver)

    def register(self, username, email, password):
        """Creates a new account"""

        self.driver.get("http://127.0.0.1:8000/account/register/")
        self.driver.maximize_window()
        sleep(3)
        user_box = self.driver.find_element_by_name("username")
        user_box.send_keys(username)

        email_box = self.driver.find_element_by_name("email")
        email_box.send_keys(email)

        passbox_1 = self.driver.find_element_by_name("password1")
        passbox_2 = self.driver.find_element_by_name("password2")

        passbox_1.send_keys(password)
        passbox_2.send_keys(password)

        submit_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div[2]/input')
        submit_btn.click()

    def login(self, username, password):
        """Logs in with newly created user"""

        self.driver.get('http://127.0.0.1:8000/account/login/')
        sleep(3)
        user_box = self.driver.find_element_by_name("username")
        user_box.send_keys(username)

        password_box = self.driver.find_element_by_name("password")
        password_box.send_keys(password)

        submit_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div/input')
        submit_btn.click()

    def recipe(self, title, time, steps, more_info):
        self.driver.get('http://127.0.0.1:8000/recipes/recipeMain')
        sleep(3)
        make_recipe_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a[2]')
        make_recipe_btn.click()

        title = self.driver.find_element_by_name('title')
        time = self.driver.find_element_by_name('maketime')
        ingredients = self.driver.find_element_by_name('ingredients')
        steps = self.driver.find_element_by_name('steps')
        more_info = self.driver.find_element_by_name('etc')

        title.send_keys(title)
        time.send_keys(time)
        ingredients.send_keys(ingredients)
        steps.send_keys(steps)
        more_info.send_keys(more_info)

        submit_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/input[3]')
        submit_btn.click()

    def add_to_cal(self):
        """adds recipe to calendar"""

        self.driver.get('http://127.0.0.1:8000/cal/')
        new_scheduled = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/a[1]')
        new_scheduled.click()
        recipe_options = self.driver.find_element_by_name('recipe')
        recipe_options.click()

        recipe = self.driver.find_element_by_xpath('/html/body/div[1]/form/table/tbody/tr[1]/td/select/option')
        recipe.click()

        time = self.driver.find_element_by_name('scheduled_date')
        today = date.today()
        time.send_keys(today)

        submit_btn = self.driver.find_element_by_xpath("/html/body/div[1]/form/table/tbody/tr[3]/td/button")
        submit_btn.click()


    def to_pantry(self):
        """Navigate to pantry site"""

        self.driver.get('http://127.0.0.1:8000/pantry')

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

    def add_forum_post(self, title, intro, body):
        """ Adds a post to the forum"""

        self.driver.get('http://127.0.0.1:8000/forum/')
        sleep(3)
        make_post_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/a[2]')
        make_post_btn.click()
        sleep(2)

        title_box = self.driver.find_element_by_name("title")
        intro_box = self.driver.find_element_by_name("intro")
        body_box = self.driver.find_element_by_name("body")

        title_box.send_keys(title)
        intro_box.send_keys(intro)
        body_box.send_keys(body)

        submit_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/form/div')
        sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)
        self.action.move_to_element(submit_btn).click().perform()


if __name__ == '__main__':
    pt = pantryTest()

    username = "garrison1"
    email = "garrison@gmail.com"
    password = "Gener1cP@ss!"

    pt.register(username, email, password)
    pt.login(username, password)

    # Test no longer works due to site changes
    # pt.to_pantry()
    # Currently, we add 10 items to the list
    # for i in range(10):
    # pt.add_item("Test Item " + str(i))

    title = "This is a fake title"
    intro = "This is a fake intro"
    body = "This is a fake body!!!!! IT is a little longer than the others just because that makes the most sense!"
    pt.add_forum_post(title, intro, body)

    time = 300
    steps ="First buy cake mix! Second bake!!"
    more_info = "You really don't need to know anything else!"
    pt.recipe(title, time, steps, more_info)
    pt.add_to_cal()
    #Testing is done. Sleep after is just to explore the website and find any potential problems
    sleep(300)