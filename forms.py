#### form.py ###

#### Creates two forms signing up and logging in ####


## Import wtforms and FlaskForm libraries to help us
from flask_wtf import FlaskForm
from wtforms import Form, SubmitField, StringField, PasswordField, validators

## Class for login form
class LoginForm(FlaskForm):
    email = StringField('email',[validators.DataRequired(),validators.Email()])
    password = PasswordField ('Password',[validators.DataRequired()])
    submit = SubmitField('Log In')

# Class for our sign up for to allow students to register.
class SignUpForm(Form):
    fname = StringField('First name',[validators.Length(min=2, max=25)])
    surname = StringField('Surname',[validators.Length(min=2, max=25)])
    email = StringField('Email',[validators.Email()])
    password = PasswordField('Password',[validators.Length(min=4, max=25), validators.EqualTo('pass_confirm',message='Passwords must match')])
    pass_confirm = PasswordField ('Confirm Password')
    code = StringField('Sign up code')
    submit = SubmitField('Register!')


class addBook(Form):
    ISBN = StringField('ISBN',[validators.Length(min=2, max=25)])
    title = StringField('Title',[validators.Length(min=2, max=25)])
    author = StringField('Author',[validators.Length(min=2, max=25)])
    submit = SubmitField('Sumbit')