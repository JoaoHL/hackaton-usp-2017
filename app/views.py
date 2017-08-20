from app import app
from app import users
from flask_mail import Message
import app.Paper as Paper
import app.mailer as mailer

@app.route('/')
@app.route('/index')
def index():
    result = "Hello World!\n"
    return result

@app.route('/checkMail')
def checkMail():
    result = "Checking mails\n"
    papers = Paper.getMockPapers()
    for ind in users:
        match = []
        for paper in papers:
            if not paper.tags.isdisjoint(ind.interests):
                match.append(paper)
        if match != []:
            try:
                mailer.sendMail(ind, match)
                result += "Sent email to " + ind.name + "\n"
            except Exception as e:
                result += "Error processing email for " + ind.name + "\n"
                result += str(e)
                raise
    return result
