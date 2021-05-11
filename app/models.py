from flask_login import UserMixin

class User():
    def __init__(self):
        pass

    def set_user(self, user):
        self.username = user[0]
        self.email = user[1]
        self.birthday = user[2]
        self.password = user[3]

    def get_email(self):
        return self.email
    
    def __repr__(self):
        return(f"{self.username} {self.email} {self.birthday} {self.password}")
