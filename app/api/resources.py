"""API """
from flask_restful import Resource, fields, marshal
from flask_login import current_user
from flask import request
import requests
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

get_portfolio_fields = {
    "stock_symbol": fields.String,
    "quantity": fields.Integer,
    "current_value": fields.Float
}

get_401_fields = {
    "response": fields.String
}


class BalanceResources(Resource):
    """HTTP API methods regarding current user's balance"""
    def get(self):
        """Returns current balance for user"""
        if current_user.is_authenticated:
            id_num = current_user.get_id()
            return  marshal(Balance.query.filter_by(user_id=id_num).first(),
                            get_balance_fields), 200

        else:
            response = {'response':'Unauthenticated. Please log in'}
            return marshal(response, get_401_fields), 401

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
        else:
            response = {'response':'Unauthenticated. Please log in'}
            return marshal(response, get_401_fields), 401


class TransactionResources(Resource):
    """HTTP API methods regarding current user's transactions"""
    def get(self):
        """Returns all transactions for user"""
        if current_user.is_authenticated:
            id_num = current_user.get_id()
            return  marshal(Transaction.query.filter_by(user_id=id_num).all(),
                            get_transaction_fields), 200
        else:
            response = {'response':'Unauthenticated. Please log in'}
            return marshal(response, get_401_fields), 401


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
        else:
            response = {'response':'Unauthenticated. Please log in'}
            return marshal(response, get_401_fields), 401

class PortfolioResources(Resource):
    """HTTP API methods getting a user's stock symbols owned and quantity for each"""
    def get(self):
        """Returns current balance for user"""
        if current_user.is_authenticated:
            id_num = current_user.get_id()
            text = "SELECT stock_symbol, SUM(quantity) as quantity FROM transactions \
                    WHERE user_id=:user_id GROUP BY stock_symbol"
            result = db.session.execute(text, {"user_id":id_num})
            portfolio_list = [{column: value for column, value in rowproxy.items()}
                              for rowproxy in result]

            symbols_list = []
            symbols_string = ","

            for row in portfolio_list:
                symbols_list.append(row["stock_symbol"])

            last_price_symbols = "https://api.iextrading.com/1.0/tops/last?symbols=" + \
                symbols_string.join(symbols_list)

            response = requests.get(last_price_symbols).json()

            new_list = []
            for portfolio_list, resp in zip(portfolio_list, response):
                new_list.append({"stock_symbol":portfolio_list['stock_symbol'],
                                 "quantity":portfolio_list['quantity'],
                                 "current_value":
                                 round(resp['price']*portfolio_list['quantity'], 2)})

            return marshal(new_list, get_portfolio_fields), 200
        else:
            response = {'response':'Unauthenticated. Please log in'}
            return marshal(response, get_401_fields), 401
            