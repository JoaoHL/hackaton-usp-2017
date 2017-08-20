##Class that models our users
class User:
    def __init__(self, name, email, interests, date):
        self.name = name
        self.email = email
        self.interests = interests
        self.date = date

##Mock users
def MockUsers():
    mockusers = []
    interest = set(['graph theory'])
    mockusers.append(User("Antonio", "antonio.augusto.abello@gmail.com", interest, "2017/01/16"))
    return mockusers
    
    
