"""Routes to portfolio and transactions pages """
from flask import render_template
from flask_login import login_required, current_user
from . import main_bp


@main_bp.route('/', methods=['GET'])
def mainpage():
    """Renders main page asking to registe or log in """
    return render_template('mainpage.html')


@main_bp.route('/portfolio', methods=['GET'])
@login_required
def portfolio():
    """Renders page to view portfolio and purchase stocks """
    return render_template('portfolio.html', name=current_user.first_name)


@main_bp.route('/transaction', methods=['GET'])
@login_required
def transaction():
    """ Renders page to view list of transactions """
    return "Hi, Please see your transactions below."
