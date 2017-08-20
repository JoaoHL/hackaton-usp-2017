#Class that models the papers
import arxivApiClient as aac

class Paper:
    def __init__(self, title, abstract, link):
        self.title = title
        self.abstract = abstract
        self.link = link

def getMockPapers():
    MockPapers = []
    tags = set(['graph theory'])
    MockPapers.append(Paper("New discovery in Graph theory", "abstract discovery", "www.link.com"))
    return MockPapers

##TO-DO: add date checking
##TO-DO: receive link
def getUserPapers(user):
    RealPapers = []
    rawinfo = aac.retrievePaperInfo(user.interests)
    for meat in rawinfo:
        meat = meat['entry']
        paper = Paper(meat['title'], meat['summary'], "")
        RealPapers.append(paper)
    return RealPapers
         
