"""This module should be able to run in the command line"""
import sys

class Menu:
    def __init__(self):
        pass


    def display_users(self):
        """This method displays the type of users we have"""
        print("""
        1. Normal User
        2. Moderator
        3. Admin
        """)

    def display_menu(self):
        """This method displays the functionality of our app"""
        print("""

        """)

    def run(self):
        """Displays the Menu and respond to choices"""
        while True:
            self.display_users()
            # action = self.choices.get()
            choose_a_user = input("Please log in as: ")
            print(choose_a_user)
            if action == "1":
                print("""
                a. Create a Comment
                b. Edit a Comment
                c. Show a Comment
                """)
                choose_a_method = input("What do you want to do?: ")
            elif action == "2":
                print("""
                a. Create a Comment
                b. Edit a Comment
                c. Show a Comment
                d. Delete a Comment
                """)
                choose_a_method = input("What do you want to do?: ")
            else:
                print("""
                a. Create a Comment
                b. Edit a Comment
                c. Show a Comment
                d. Delete a Comment
                """)
                choose_a_method = input("What do you want to do?: ")


if __name__ == "__main__":
    Menu().run()