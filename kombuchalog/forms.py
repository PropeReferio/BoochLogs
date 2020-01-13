from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email#, length
from flask_wtf import FlaskForm

class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(),Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_pass = PasswordField("Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")

class LogForm(FlaskForm):
    f1date = StringField("1st Fermentation Start Date", validators=[DataRequired()])
    f1duration = StringField("1st Fermentation Duration", validators=[DataRequired()])
    flavors = StringField("Flavors added", validators=[DataRequired()])
    f2date = StringField("2nd Fermnation Start Date", validators=[DataRequired()])
    f2duration = StringField("2nd Fermentation Duration", validators=[DataRequired()])
    rating = StringField("1 to 5 rating", validators=[DataRequired()])
    notes = StringField("Notes") #Condsider TextField here
    submit = SubmitField("Submit")