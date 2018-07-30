import datetime


class Users:

    def __init__(self, ):
        # Initialize the user model.
        self.login = datetime.datetime.now()

    def create_comment(self):
        pass

    def read_comment(self):
        pass

    def update_comment(self):
        pass


class Moderator(Users):
    """Moderator class adds the functionality to delete comment"""
    def update_comment(self, author='moderator'):
        pass

    def delete_comment(self):
        pass


class Admin(Moderator):
    """Adds the functionality to delete and edit all users comments"""
    


