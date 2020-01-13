from flask_sqlalchemy import SQLAlchemy
from kombuchalog import app, db
from werkzeug.security import generate_password_hash
from datetime import datetime


from kombuchalog import login
from flask_login import UserMixin



@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    post = db.relationship('Log', backref = 'author', lazy=True)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password,salt_length=10)
        return self.pw_hash

    def __repr__(self):
        return 'User {} has been created.'.format(self.username)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f1date = db.Column(db.String(20))
    f1duration = db.Column(db.String(10))
    flavors = db.Column(db.String(200))
    f2date = db.Column(db.String(20))
    f2duration = db.Column(db.String(10))
    rating = db.Column(db.String(10))
    notes = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return "This brew was made by {} with these flavors: {}".format(self.user_id, self.flavors)