##script to format and send emails
import app.User
import app.Paper
from app import mail
from flask_mail import Message
from flask import render_template

def sendMail(user, papers, debug=False):
    print("Sending mail")
    msg = Message("New papers!", sender=("Sciternews", "sciternews@hotmail.com"))
    msg.recipients = [user.email]
    msg.html = render_template("template-mail.html", papers=papers, user=user)

    if debug:
        return msg.html
    else:
        mail.send(msg)
        
        
