from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class RegisterForm(FlaskForm):
    first_name = StringField('First name: ', validators = [InputRequired('Please provide your first name.')])
    last_name = StringField('Last name: ', validators = [InputRequired('Please provide your last name.')])
    email= StringField('Email: ', 
                    validators = [InputRequired("An email address is required"), 
                    Email(message="Please submit a valid email.")])
    passphrase = PasswordField('Passphrase: ', validators = [InputRequired("A Passphrase is required."),
                    Length(min=16, message="Your passphrase must have a minimum of 16 characters.")])

class LoginForm(FlaskForm):
    email= StringField('Email: ', 
                    validators = [InputRequired("An email address is required"), 
                    Email(message="Please submit a valid email.")])
    passphrase = PasswordField('Passphrase: ', validators = [InputRequired("A Passphrase is required."),
                    Length(min=16, message="Your passphrase must have a minimum of 16 characters.")])

        