"""admin and privileges modules"""

from userchap9ex import User

class Admin(User):
    def __init__(self, first_name, last_name, username, password, access_level):
        """initialize the admin"""
        super().__init__(first_name, last_name, username, password, access_level)
    #     self.privileges = ['can add post', 'can delete post', 'can ban user']
        self.privileges = Privileges()
    
    # def show_privileges(self):
    #     """show the privileges an admin has"""
    #     print(f"An admin has the following privileges:")
    #     for privilege in self.privileges:
    #         print(privilege)


#9.8 - requires 9.7 to be live but privileges commented
class Privileges:
    """Outline the privileges an admin has."""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """show the privileges an admin has"""
        print(f"An admin has the following privileges:")
        for privilege in self.privileges:
            print(privilege)