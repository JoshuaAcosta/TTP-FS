from app import db
from flask import render_template, url_for, redirect, request, flash
from flask import current_app as app
from app.models import User
from flask_login import login_user, logout_user, login_required
from .forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from . import auth_bp

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email').lower()
            passphrase = request.form.get('passphrase')
            
            existing_user = User.query.filter_by(email=email).first()

            if existing_user is None:
                new_user = User(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    passphrase=generate_password_hash(passphrase, method='sha256'),
                    balance=5000.00
                    )
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect(url_for('main.portfolio'))
            else:
                flash('An account for this email address already exists.')
                return redirect(url_for('auth.register'))

    return render_template('register.html', form=form)

@auth_bp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            email = request.form.get('email').lower()
            passphrase = request.form.get('passphrase')

            user = User.query.filter_by(email=email).first()

            if user and check_password_hash(user.passphrase, passphrase): 
                login_user(user)
                return redirect(url_for('main.portfolio'))
            else:
                flash('Please check your login details and try again.')
                return redirect(url_for('auth.login'))

    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))