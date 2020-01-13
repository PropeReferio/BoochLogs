
from kombuchalog import app, db
from flask import render_template, url_for, request, redirect
from kombuchalog.forms import SignUpForm, LoginForm, LogForm


from werkzeug.security import check_password_hash


from flask_login import login_user, current_user, login_required


from kombuchalog.models import User, Log

#Home Route
@app.route("/")
def home():

    posts = Log.query.all()
    return render_template("home.html")#, post = posts) watch double parentheses

#Signup Route
@app.route("/signup", methods=["GET", "POST"])
def signup():
    signUpForm = SignUpForm()
    if request.method == "POST":
        username = signUpForm.username.data
        email = signUpForm.email.data
        password = signUpForm.password.data
        print(username, email, password)
        #Next, move this stuff to the database.
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()

    return render_template("signup.html", signupform = signUpForm) 

@app.route("/login", methods=["GET", "POST"])
def login():
    loginForm = LoginForm()
    if request.method == "POST":
        user_email = loginForm.email.data
        password = loginForm.password.data
        logged_user = User.query.filter(User.email == user_email).first()
        if logged_user and check_password_hash(logged_user.password,password):
            login_user(logged_user)
            print(current_user.username)
            return redirect(url_for('home'))
    else:
        print("Not Valid Method")
    return render_template("login.html", loginform = loginForm)

@app.route('/log', methods=["GET", "POST"])
@login_required
def log():
    logForm = LogForm()
    if request.method == "POST":
        f1date = logForm.f1date.data
        f1duration = logForm.f1duration.data
        flavors = logForm.flavors.data
        f2date = logForm.f2date.data
        f2duration = logForm.f2duration.data
        rating = logForm.rating.data
        notes = logForm.notes.data
        user_id = current_user.id
        print(f1duration,flavors)
        #Save to DataBase
        log = Log(f1date=f1date, f1duration=f1duration, flavors=flavors, \
f2date=f2date, f2duration=f2duration, rating=rating, notes=notes)
        db.session.add(log)
        db.session.commit()

    return render_template("addbrew.html", logform = logForm)