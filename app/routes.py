from app import db
from flask import render_template, url_for, redirect, request, flash
from flask import current_app as app
from.models import User
from .forms import RegisterForm
from werkzeug.security import generate_password_hash

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            name = request.form.get('name')
            email = request.form.get('email').lower()
            passphrase = request.form.get('passphrase')
            
            existing_user = User.query.filter_by(email=email).first()

            if existing_user is None:
                new_user = User(
                    name=name,
                    email=email,
                    passphrase=generate_password_hash(passphrase, method='sha256'),
                    balance=5000.00
                    )
                db.session.add(new_user)
                db.session.commit()
                #login_user(user)
                return redirect(url_for('portfolio'))
            else:
                flash('An account for this email address already exists.')
                return redirect(url_for('register'))

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET'])
def login():
    return "SIGN IN"

@app.route('/portfolio', methods=['GET'])
def portfolio():
    return "Hi, Please see your portfolio below."
