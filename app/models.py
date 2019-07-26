"""Database models"""
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    """table listing users and their log in information """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passphrase = db.Column(db.String(), nullable=False)
    transactions = db.relationship('Transaction', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def get_user_id(self):
        """ Returns user's id"""
        return self.id


class Transaction(db.Model):
    """table listing all transactions """
    __tablename__ = "transactions"

    transaction_id = db.Column(db.Integer, primary_key=True)
    stock_symbol = db.Column(db.String(5), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)
    date_purchased = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class Balance(db.Model):
    """stores users cash balance """
    __tablename__ = "balances"

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    balance = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name
