from time import sleep

from tests import AllTests 

def main():
    """Tests the main account functionality"""

    # Construct the tester
    tester = AllTests()

    # Register and login
    username = "garrison2"
    email = "garrison@gmail.com"
    password = "Gener1cP@ss!"
    tester.register(username, email, password)
    tester.login(username, password)
    sleep(1)

    # Add a recipe and add it to calendar
    title = "This is a fake title"
    time = 300
    ingredients = "Cake mix"
    steps ="First buy cake mix! Second bake!!"
    more_info = "You really don't need to know anything else!"
    tester.add_recipe(title, time, ingredients, steps, more_info)

    # Schedule the recipe to today's date
    tester.schedule_recipe_from_recipes()

    # Edit the recipe
    tester.edit_recipe()

    # Delete the recipe
    tester.delete_recipe()

    # Testing is done. Sleep after is just to explore the website and find any potential problems
    sleep(300)

if __name__ == "__main__":
    main()