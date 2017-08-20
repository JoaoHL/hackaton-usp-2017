import arxivApiClient as aac

#Utility functions
def dateFormating(publdate):
    publdate = publdate.split("T")[0]
    publdate = publdate.replace("-", "/")
    return publdate

#inteligent clipping, dont clip words
def clipTitle(title):
    divtitle = title.split(" ")
    numchars = 0
    restitle = ""
    for i in range(len(divtitle)):
        if numchars < 40:
            restitle += divtitle[i] + " " 
            numchars += len(divtitle[i]) + 1 
        else:
            restitle += "..."
            break
    return restitle
    

#Class that models the papers
class Paper:
    def __init__(self, title, abstract, link, author, published):
        self.title = title
        self.abstract = abstract
        self.link = link
        self.author = author
        self.published = published

def getMockPapers():
    MockPapers = []
    MockPapers.append(Paper("New discovery in Graph theory", "abstract discovery", "www.link.com"))
    return MockPapers

##TO-DO: add date checking
##TO-DO: receive link
def getUserPapers(user):
    RealPapers = []
    rawinfo = aac.retrievePaperInfo(user.interests)
    for meat in rawinfo:
        meat = meat['entry']
        paper = Paper(clipTitle(meat['title']), meat['summary'], meat['id'], meat['author'], dateFormating(meat['published']))
        RealPapers.append(paper)
    return RealPapers
         

