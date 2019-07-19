from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class RegisterForm(FlaskForm):
    name = StringField('Full name: ', validators = [InputRequired('Please provide your full name.')])
    email= StringField('Email: ', 
                    validators = [InputRequired("An email address is required"), 
                    Email(message="Please submit a valid email.")])
    passphrase = PasswordField('Passphrase: ', validators = [InputRequired("A Passphrase is required."),
                    Length(min=16, message="Your passphrase must have a minimum of 16 characters.")])