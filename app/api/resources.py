from flask import jsonify
from flask_restful import Resource
from app.models import Balance
from flask_login import current_user


class BalanceResources(Resource):
    def get(self):
        if current_user.is_authenticated:
            id_num = current_user.get_id()
            current_user_balance = Balance.query.filter_by(user_id=id_num).first()
            return jsonify(float(current_user_balance.balance))
        