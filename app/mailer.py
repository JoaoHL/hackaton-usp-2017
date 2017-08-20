##script to format and send emails
import app.User
import app.Paper
from app import mail
from flask_mail import Message

def sendMail(user, papers):
    print("Sending mail")
    msg = Message("New papers!")
    msg.recipients = [user.email]
    body = ""
    for paper in papers:
        body += "Paper: " + paper.title + "\n"
        body += "abstract: " + paper.abstract + "\n"
        body += "link: " + paper.link + "\n"
    msg.body = body
    print("Body: " + body)
    mail.send(msg)
        
        
