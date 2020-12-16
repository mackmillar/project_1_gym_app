class Member:
    def __init__(self, name, email, premium, id = None):
        self.name = name
        self.email = email
        self.premium = premium
        self.id = id


    def premium_member(self):
        self.premium = True