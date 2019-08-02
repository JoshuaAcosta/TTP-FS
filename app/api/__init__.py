"""API implementation """
from flask import Blueprint
from flask_restful  import Api
from .resources import BalanceResources, TransactionResources

api_bp = Blueprint('api', __name__)

api = Api(api_bp)

api.add_resource(BalanceResources, '/api/balance/me', methods=["GET", "PUT"])
api.add_resource(TransactionResources, '/api/transaction/me', methods=["GET", "POST"])
