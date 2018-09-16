from flask import Flask, render_template, url_for, flash, redirect
from Account import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '86a96f50cbfe444358b8'

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


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'jam@jimblobulate.com' and form.password.data == "password":
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
