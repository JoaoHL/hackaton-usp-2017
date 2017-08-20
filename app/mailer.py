##script to format and send emails
import app.User
import app.Paper
from app import mail
from flask_mail import Message
from flask import render_template

def sendMail(user, papers, debug=False):
    print("Sending mail")
    msg = Message("New papers!")
    msg.recipients = [user.email]
    """
    body = ""
    for paper in papers:
        body += "Paper: " + paper.title + "\n"
        body += "abstract: " + paper.abstract + "\n"
        body += "link: " + paper.link + "\n"
    msg.body = body
    """
    msg.html = render_template("template-mail.html", papers=papers, user=user)

    if debug:
        return msg.html
    else:
        mail.send(msg)
        
        
