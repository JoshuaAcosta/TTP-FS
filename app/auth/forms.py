"""Authorization forms used to create and login users """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, Regexp


class RegisterForm(FlaskForm):
    """Registration form with email and strong password validators """
    first_name = StringField(
        'First name: ', validators=[
            InputRequired('Please provide your first name.')])

    last_name = StringField(
        'Last name: ', validators=[
            InputRequired('Please provide your last name.')])

    email = StringField(
        'Email: ', validators=[InputRequired("An email address is required"),
                               Email(message="Please submit a valid email.")])
    passphrase = PasswordField(
                'Passphrase: ', validators=[
                    InputRequired("A Passphrase is required."),
                    Length(min=16, message="Your passphrase must\
                                            have a minimum of 16 characters."),
                    Regexp(regex="(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])\
                                    (?=.*?[!\"#$%&'()*+,-./:;<=>?@[]^_`{|}~])",
                           message="Your passphrase must contain atleast one uppercase\
                                           letter, one lowercase letter, one\
                                           number and a special character.")])


class LoginForm(FlaskForm):
    """Log in form requiring email and passwords fields"""
    email = StringField(
        'Email: ', validators=[
            InputRequired("An email address is required"),
            Email(message="Please submit a valid email.")])
    passphrase = PasswordField(
                'Passphrase: ', validators=[
                    InputRequired("A Passphrase is required."),
                    Length(min=16, message="Your passphrase must\
                                        have a minimum of 16 characters.")])
