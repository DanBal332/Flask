import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from Flask.Flask1 import app, db, bcrypt
from Flask.Flask1.Account_form import RegistrationForm, LoginForm, UpdateAccountForm
from Flask.Flask1.models import User
from flask_login import login_user, current_user, logout_user, login_required


# Example posts
posts = [
    {
        "author": "Jame",
        "title": "Mon nom Jean",
        "content": "Hi, my name is Jame!"
    },
    {
        "author": "Jam",
        "title": "Mon nom Jam",
        "content": "i am the overlord Jean Bob!"
    }
]

# Creating routes for different pages
# Home page route


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

# About page route


@app.route("/about")
def about():
    return render_template('about.html', title='About')

# Registration page route


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    # Adding data to database and hashing + salting password
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

# Login page route


@app.route("/login", methods=["GET", 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    # Validating user data from database
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# Logout page route redirecting to Home page


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.route_path, 'static/profile_pics', picture_fn)
    form_picture.save(picture_path)
    return picture_fn

# Account page route


@app.route("/account", methods=["GET", 'POST'])
@login_required
# Returning user's data to see on Account page
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.image_file = form.image_file.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

