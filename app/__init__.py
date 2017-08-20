from flask import Flask
from flask_mail import Mail
import app.User
import app.Paper
import app.configs as configs

app = Flask(__name__)

##Mail configuration
app.configs = configs.config
mail = Mail(app)
users = User.MockUsers()
from app import views

