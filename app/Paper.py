import arxivApiClient as aac

#Utility functions
def dateFormating(publdate):
    publdate = publdate.split("T")[0]
    publdate = publdate.replace("-", "/")
    return publdate

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

def getMockPapers():
    MockPapers = []
    tags = set(['graph theory'])
    MockPapers.append(Paper("New discovery in Graph theory", "Grahl Phillip Theodore Ryan", "ect to second tier occasional objects, but most newspapers Watterson's stocking; the Noodle American middle-class and shallowings just commonly birthday celebrate this,' says he have quited for full, third, and the Lacanian Real, with commentary and ice craft of medication' accompanied by Cartoon strips Few editors appear This half of a new present time you were happen against walls, demand rambunction The Duplicator can be stopping Calvin's serve to ask for, often she supposed to fit this whole life\n" \
   "Watterson had comic books, public decides to market the strip, I wasn't again theories of dollars person Calvin's creation, the open for press refuses together with howling, purposed a unique Easter egg instructor in the Complete, and greated at an 'anatomicalled Calvin, echoing Watterson and the childhood animation spell anything certain things'\n"\
   "Remaining dinosaurs In a notabloid and civilized Her relations and the Transrelation,' and camping me", "http://www.link.com", "22/02/2017"))
    MockPapers.append(Paper("Another Interesting Paper", "Joseph Rabbit", "This is a quite interesting abstract about my paper, you should really check it out", "http://www.google.com.br", "22/02/2016"))
    MockPapers.append(Paper("My Hackathon Paper", "Anthony John Lucian", "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?", "http://www.facebook.com", "22/02/2015"))
    return MockPapers

##TO-DO: add date checking
##TO-DO: receive link
def getUserPapers(user):
    RealPapers = []
    rawinfo = aac.retrievePaperInfo(user.interests)
    for meat in rawinfo:
        meat = meat['entry']
        paper = Paper(clipText(meat['title'], 30), meat['author'], clipText(meat['summary'], 140), meat['id'], dateFormating(meat['published']))
        RealPapers.append(paper)
    return RealPapers
         

