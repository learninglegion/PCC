"""module that pulls together all of the user and admin classes"""

class User:
    def __init__(self, first_name, last_name, username, password, access_level):
        """initialize the user"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.access_level = access_level
        self.login_attempts = 0

    def describe_user(self):
        """describe the user"""
        print(f"Acessing database for {self.username}:\n")
        print(f"First name: {self.first_name.title()} Last name: {self.last_name.title()}")
        print(f"Password: {self.password} Access level: {self.access_level}")
        
    def greet_user(self):
        """Greet the user on login"""
        print(f"Hello again, {self.username}.")
    
    def increment_login_attempts(self):
        """Increase numberof login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Set login attempts back to 0"""
        self.login_attempts = 0

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