from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Making instances
app = Flask(__name__)
# Secret key against CSRF attacks (Cross Sight Request Forgery)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# Making file which will be used as database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///web.database'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from Flask.Flask1 import routes
