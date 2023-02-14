from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from core.settings import create_path_to_db, Config


db = SQLAlchemy()

login_manager = LoginManager()


def register_extensions(app):

    db.init_app(app)

    login_manager.init_app(app)


def register_blueprints(app):
    from core.routes import main
    from core.user.routes import users

    app.register_blueprint(main)
    app.register_blueprint(users)


def configure_database(app):
    create_path_to_db()

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    configure_database(app)
    register_blueprints(app)

    return app
