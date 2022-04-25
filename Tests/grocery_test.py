from time import sleep

from tests import AllTests 

def main():
    """Tests the main grocery functionality.
    Adds grocery items, sends them to the pantry, then deletes the items from both.
    """

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

    # Send grocery items to the pantry
    tester.send_grocery_to_pantry()

    # Delete items from the pantry
    tester.clear_pantry()

    # Delete items from grocery
    tester.clear_grocery_items()

    # Testing is done. Sleep after is just to explore the website and find any potential problems
    sleep(300)

if __name__ == "__main__":
    main()