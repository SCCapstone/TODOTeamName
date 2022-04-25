from time import sleep

from tests import AllTests 

def main():
    """Tests the main forum functionality.
    Adds a forum post, adds a comment, then deletes the post. 
    """

    # Construct the tester
    tester = AllTests()

    # Register and login
    username = "garrison2"
    email = "garrison@gmail.com"
    password = "Gener1cP@ss!"
    tester.register(username, email, password)
    tester.login(username, password)

    # Add a forum post
    title = "This is a fake title"
    intro = "This is a fake intro"
    body = "This is a fake body!!!!! It is a little longer than the others just because that makes the most sense!"
    tester.add_forum_post(title, intro, body)

    # Add a comment to the forum post
    tester.add_comment(username, email, body)

    # Delete the forum post
    tester.delete_forum_post()

    # Testing is done. Sleep after is just to explore the website and find any potential problems
    sleep(300)


if __name__ == "__main__":
    main()