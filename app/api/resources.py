"""API """
from flask_restful import Resource, fields, marshal_with
from flask_login import current_user
from flask import request
from app.models import Balance, Transaction
from app import db


get_balance_fields = {
    'user_id': fields.Integer,
    'balance': fields.Float
}

get_transaction_fields = {
    "transaction_id": fields.Integer,
    "stock_symbol": fields.String,
    "quantity": fields.Integer,
    "date_purchased": fields.DateTime,
    "user_id": fields.Integer
}


class BalanceResources(Resource):
    """HTTP API methods regarding current user's balance"""
    @marshal_with(get_balance_fields)
    def get(self):
        """Returns current balance for user"""
        if current_user.is_authenticated:
            id_num = current_user.get_id()
            return  Balance.query.filter_by(user_id=id_num).first()

    def put(self):
        """Updates current user's balance"""
        if (current_user.is_authenticated) and (request.method == 'PUT'):
            data = request.get_json()
            new_balance = data["new_balance"]
            id_num = current_user.get_id()
            user_new_balance = Balance.query.filter_by(user_id=id_num).first()
            user_new_balance.balance = new_balance
            db.session.commit()
            return {"result":"success"}


class TransactionResources(Resource):
    """HTTP API methods regarding current user's transactions"""
    @marshal_with(get_transaction_fields)
    def get(self):
        """Returns all transactions for user"""
        if current_user.is_authenticated:
            id_num = current_user.get_id()
            return Transaction.query.filter_by(user_id=id_num).all()

    def post(self):
        """Post new transaction completed into db, returns successful status"""
        if (current_user.is_authenticated) and (request.method == 'POST'):
            data = request.get_json()

            stock_symbol = data["stock_symbol"]
            quantity = data["quantity"]
            date_purchased = data["date_purchased"]
            user_id = current_user.get_id()

            new_transactions = Transaction(
                stock_symbol=stock_symbol,
                quantity=quantity,
                date_purchased=date_purchased,
                user_id=user_id
                )
            db.session.add(new_transactions)
            db.session.commit()

            return {"result":"success"}
