from flask import render_template, redirect, flash
from app import app
from app import users
from flask_mail import Message
from .forms import UserPreferences
import app.Paper as Paper
import app.mailer as mailer

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserPreferences()
    if form.validate_on_submit():
        print("Vou cadastrar o usuario {} com email {} e preferencias {}".format(form.name.data, form.email.data, form.areas_of_interest.data))
        return redirect('/show_papers')
    return render_template('index.html',
            form=form)

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

@app.route('/debugMail')
def debugMail():
    for ind in users:
        papers = Paper.getUserPapers(ind)
        return mailer.sendMail(ind, papers, debug=True)
    
@app.route('/show_papers', methods=['GET'])
def show_papers():
    papers = Paper.getPapersForView()
    papers = papers[:10]
    return render_template('papers.html', papers=papers)
