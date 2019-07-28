from flask import Blueprint
from flask_restful  import Api
from .resources import BalanceResources

api_bp = Blueprint('api', __name__)

api = Api(api_bp)

api.add_resource(BalanceResources, '/api/balance/me')
