##Class that models our users
class User:
    def __init__(self, name, email, interests):
        self.name = name
        self.email = email
        self.interests = interests

##Mock users
def MockUsers():
    mockusers = []
    interest = set(['graph'])
    mockusers.append(User("Antonio", "antonio.augusto.abello@gmail.com", interest))
    return mockusers
    
    
