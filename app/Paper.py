#Class that models the papers
class Paper:
    def __init__(self, title, abstract, link, tags):
        self.title = title
        self.abstract = abstract
        self.link = link
        self.tags = tags

def getMockPapers():
    MockPapers = []
    tags = set(['graph theory'])
    MockPapers.append(Paper("New discovery in Graph theory", "abstract discovery", "www.link.com", tags))
    return MockPapers
