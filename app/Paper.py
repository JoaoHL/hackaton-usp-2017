import arxivApiClient as aac

#Utility functions
def dateFormating(publdate):
    publdate = publdate.split("T")[0]
    publdate = publdate.replace("-", "/")
    return publdate

#dates are strings "YYYY/MM/DD"
def compareDate(date1, date2):
    date1 = list(map(int, date1.split('/')))
    date2 = list(map(int, date2.split('/')))
    for i in range(len(date1)):
        if date1[i] > date2[i]:
            return True
        elif date1[i] < date2[i]:
            return False
    return False

#inteligent clipping, dont clip words
def clipText(title, treshold):
    divtitle = title.split(" ")
    numchars = 0
    restitle = ""
    for i in range(len(divtitle)):
        if numchars < treshold:
            restitle += divtitle[i] + " " 
            numchars += len(divtitle[i]) + 1 
        else:
            restitle += "..."
            break
    return restitle
    

#Class that models the papers
class Paper:
    def __init__(self, title, author, abstract, link, published):
        self.title = title
        self.author = author
        self.abstract = abstract
        self.link = link
        self.published = published

##TO-DO: add date checking
##TO-DO: receive link
def getUserPapers(user):
    RealPapers = []
    rawinfo = aac.retrievePaperInfo(user.interests)
    for meat in rawinfo:
        meat = meat['entry']
        if compareDate(dateFormating(meat['published']), user.date):
            paper = Paper(clipText(meat['title'], 40), meat['author'], clipText(meat['summary'], 140), meat['id'], dateFormating(meat['published']))
            RealPapers.append(paper)
    return RealPapers
         
def getPapersForView():
    papers = []
    rawinfo = aac.retrievePaperInfo(set(["Graph Theory"]))
    for meat in rawinfo:
        meat = meat['entry']
        paper = Paper(clipText(meat['title'], 100), meat['author'], clipText(meat['summary'], 1500), meat['id'], dateFormating(meat['published']))
        papers.append(paper)
    return papers
