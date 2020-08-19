class User:

    
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email


    def get_first_name(self):
        return self.first_name


    def get_last_name(self):
        return self.last_name


    def get_email(self):
        return self.email


    def set_first_name(self, first_name):
        self.first_name = first_name


    def set_last_name(self, last_name):
        self.last_name = last_name


    def set_email(self, email):
        self.email = email

