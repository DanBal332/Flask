from datetime import datetime
from Flask.Flask1 import db, login_manager
from flask_login import UserMixin


# Making a function that will fetch user data from database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Making a class that will make sure that users filled out registration form validly
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='/Users/danb/PycharmProjects/Flask2/Flask'
                                                                  '/Flask1/static/profile_pics/default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # Stating how the data will be printed
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


# Making the class that will act as the post structure
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Stating how the data will be printed
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
