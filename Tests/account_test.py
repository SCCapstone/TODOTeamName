from time import sleep

from tests import AllTests 

def main():
    """Tests the main account functionality.
    Registers, logs in, and edits the user profile.
    """

    # Construct the tester
    tester = AllTests()

    # Register and login
    username = "garrison2"
    email = "garrison@gmail.com"
    password = "Gener1cP@ss!"
    tester.register(username, email, password)
    tester.login(username, password)

    # Edit profile
    profilename = "test name"
    allergies = "test allergies"
    tester.edit_profile(profilename, allergies)

    # Testing is done. Sleep after is just to explore the website and find any potential problems
    sleep(300)

if __name__ == "__main__":
    main()