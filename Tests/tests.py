from datetime import date
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc


class AllTests():
    """Tests the core functionality of the application"""

    def __init__(self):
        self.driver = uc.Chrome()
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()

    def register(self, username, email, password):
        """Creates a new account"""

        self.driver.get("http://127.0.0.1:8000/account/register/")
        sleep(1)
        self.driver.find_element(by=By.NAME, value="username").send_keys(username)
        self.driver.find_element(by=By.NAME, value="email").send_keys(email)
        self.driver.find_element(by=By.NAME, value="password1").send_keys(password)
        self.driver.find_element(by=By.NAME, value="password2").send_keys(password)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form/div[2]/input").click()
        sleep(1)

    def login(self, username, password):
        """Logs in with newly created user"""

        self.driver.get('http://127.0.0.1:8000/account/login/')
        sleep(1)
        self.driver.find_element(by=By.NAME, value="username").send_keys(username)
        self.driver.find_element(by=By.NAME, value="password").send_keys(password)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form/div/input").click()
        sleep(1)

    def edit_profile(self, profilename, allergies):
        """Edits profile info of the logged in user"""

        self.driver.get('http://127.0.0.1:8000/account/profile/')
        sleep(1)
        self.driver.find_element(by=By.NAME, value="name").clear()
        self.driver.find_element(by=By.NAME, value="name").send_keys(profilename)
        self.driver.find_element(by=By.NAME, value="allergy_list").clear()
        self.driver.find_element(by=By.NAME, value="allergy_list").send_keys(allergies)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form/div[2]/input").click()
        sleep(1)

    def add_recipe(self, title, time, ingredients, steps, more_info):
        """Adds a new recipe"""

        self.driver.get('http://127.0.0.1:8000/recipes/recipeMain')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/a[2]").click()
        sleep(1)
        self.driver.find_element(by=By.NAME, value="title").send_keys(title)
        self.driver.find_element(by=By.NAME, value="maketime").send_keys(time)
        self.driver.find_element(by=By.NAME, value="ingredients").send_keys(ingredients)
        self.driver.find_element(by=By.NAME, value="steps").send_keys(steps)
        self.driver.find_element(by=By.NAME, value="etc").send_keys(more_info)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form/input[3]").click()
        sleep(1)

    def schedule_recipe_from_recipes(self):
        """Schedules a recipe, from the recipes page"""

        self.driver.get('http://127.0.0.1:8000/recipes/recipeMain')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[text()='This is a fake title']").click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/form/button[1]").click()
        self.driver.find_element(by=By.NAME, value="date").send_keys(date.today().strftime("%m-%d-%Y"))
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/form/button").click()
        sleep(1)
        self.driver.get('http://127.0.0.1:8000/cal/')
        sleep(1)
    
    def edit_recipe(self):
        """Edits the content of a recipe"""

        self.driver.get('http://127.0.0.1:8000/recipes/recipeMain')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[text()='This is a fake title']").click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/form/button[2]").click()
        sleep(1)
        self.driver.find_element(by=By.NAME, value="title").send_keys(" EDITED")
        self.driver.find_element(by=By.NAME, value="ingredients").send_keys(" EDITED")
        self.driver.find_element(by=By.NAME, value="steps").send_keys(" EDITED")
        self.driver.find_element(by=By.NAME, value="etc").send_keys(" EDITED")
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/form/input[3]").click()
        sleep(1)

    def delete_recipe(self):
        """Deletes a recipe"""

        self.driver.get('http://127.0.0.1:8000/recipes/recipeMain')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="//*[contains(text(), 'This is a fake title')]").click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/form/button[3]").click()
        sleep(1)
        Alert(self.driver).accept()
        sleep(1)

    def schedule_recipe_from_cal(self):
        """Adds a recipe to the calendar"""

        self.driver.get('http://127.0.0.1:8000/cal/')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div/a[1]").click()
        sleep(1)
        self.driver.find_element(by=By.NAME, value="recipe").click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/form/table/tbody/tr[1]/td/select/option[2]").click()
        sleep(1)
        self.driver.find_element(by=By.NAME, value="scheduled_date").send_keys(date.today().strftime("%m-%d-%Y"))
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/form/table/tbody/tr[3]/td/button").click()
        sleep(1)

    def delete_scheduled_recipe(self):
        """Deletes a scheduled recipe from the calendar"""

        self.driver.find_element(by=By.XPATH, value="//*[contains(text(), '"+str(date.today().day)+"')]").click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/table/tbody/tr[2]/td/ul/li[1]/a[2]/button").click()
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/form/table/tbody/tr/td/button").click()
        sleep(1)
        
    def add_pantry_items(self, num_items):
        """Adds (num_items) items to the pantry"""

        self.driver.get('http://127.0.0.1:8000/pantry')
        sleep(1)
        for i in range(num_items):
            self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form[1]/p[1]/span/span[1]/span").click()
            self.driver.find_element(by=By.XPATH, value="/html/body/span/span/span[1]/input").send_keys("Test item "+str(i+1))
            sleep(1)
            self.driver.find_element(by=By.XPATH, value="/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
            self.driver.find_element(by=By.NAME, value="expiration").send_keys(date.today().strftime("%m-%d-%Y"))
            self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form[1]/input[2]").click()
        sleep(1)

    def clear_pantry(self):
        """Deletes all items in the pantry"""

        self.driver.get('http://127.0.0.1:8000/pantry')
        sleep(1)
        count = len(self.driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form[2]/ul/li"))
        while count > 0:
            self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form[2]/ul/li[1]/button[2]").click()
            count = count - 1
        sleep(1)

    def add_grocery_items(self, num_items):
        """Adds (num_items) items to grocery"""

        self.driver.get('http://127.0.0.1:8000/grocery')
        sleep(1)
        for i in range(num_items):
            self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form[1]/p[1]/span/span[1]/span").click()
            self.driver.find_element(by=By.XPATH, value="/html/body/span/span/span[1]/input").send_keys("Test item "+str(i+1))
            sleep(1)
            self.driver.find_element(by=By.XPATH, value="/html/body/span/span/span[1]/input").send_keys(Keys.ENTER)
            self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form[1]/input[2]").click()
        sleep(1)
    
    def send_grocery_to_pantry(self):
        """Sends grocery list over to pantry"""
        
        self.driver.get('http://127.0.0.1:8000/grocery')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form[2]/button[1]").click()
        sleep(1)
        self.driver.get('http://127.0.0.1:8000/pantry')
        sleep(1)

    def clear_grocery_items(self):
        """Deletes all grocery items"""

        self.driver.get('http://127.0.0.1:8000/grocery')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form[2]/button[2]").click()
        sleep(1)

    def add_forum_post(self, title, intro, body):
        """ Adds a post to the forum"""

        self.driver.get('http://127.0.0.1:8000/forum/')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/a[2]").click()
        sleep(1)
        self.driver.find_element(by=By.NAME, value="title").send_keys(title)
        self.driver.find_element(by=By.NAME, value="intro").send_keys(intro)
        self.driver.find_element(by=By.NAME, value="body").send_keys(body)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/form/div/button").click()
        sleep(1)

    def add_comment(self, name, email, body):
        """Adds a comment on most recent forum post """

        self.driver.get('http://127.0.0.1:8000/forum/')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div[1]/a").click()
        sleep(1)
        self.driver.find_element(by=By.NAME, value="name").send_keys(name)
        self.driver.find_element(by=By.NAME, value="email").send_keys(email)
        self.driver.find_element(by=By.NAME, value="body").send_keys(body)
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/form/div/button").click()
        sleep(1)

    def delete_forum_post(self):
        """Deletes the most recent forum post"""

        self.driver.get('http://127.0.0.1:8000/forum/')
        sleep(1)
        self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div[1]/form/button").click()
        sleep(1)
        Alert(self.driver).accept()
        sleep(1)