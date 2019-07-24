from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    if app.config['ENV'] == "production":
        app.config.from_object("config.ProductionConfig")
    elif app.config['ENV'] == "testing":
        app.config.from_object("config.TestingConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():

        from app.auth import auth_bp
        app.register_blueprint(auth_bp)

        from app.main import main_bp
        app.register_blueprint(main_bp)

        db.create_all()

    return app
