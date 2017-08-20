from flask import Flask
from flask_mail import Mail
import app.User
import app.Paper

##Username, password, etc. Not commited
import app.configs as configs

app = Flask(__name__)
app.config.from_object('config')

##Mail configuration
app.config.update(configs.config)
mail = Mail(app)
users = User.MockUsers()
from app import views


