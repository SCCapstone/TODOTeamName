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

    # Add 10 grocery items
    tester.add_grocery_items(10)

    tester.send_grocery_to_pantry()

    tester.clear_pantry()

    tester.clear_grocery_items()

    # Testing is done. Sleep after is just to explore the website and find any potential problems
    sleep(300)

if __name__ == "__main__":
    main()