from . import main_bp
from flask import render_template
from flask_login import login_required


@main_bp.route('/', methods=['GET'])
def mainpage():
    return render_template('mainpage.html')

@main_bp.route('/portfolio', methods=['GET'])
@login_required
def portfolio():
    return "Hi, Please see your portfolio below."

@main_bp.route('/transaction', methods=['GET'])
@login_required
def transaction():
    return "Hi, Please see your transactions below."