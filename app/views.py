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
    for ind in users:
        papers = Paper.getUserPapers(ind)
        try:
            mailer.sendMail(ind, papers)
            result += "Sent email to " + ind.name + "\n"
        except Exception as e:
            result += "Error processing email for " + ind.name + "\n"
            result += str(e)
    return result
