from flask import Flask
from flask_wtf import CSRFProtect
from app.config.config import get_config_by_name
from app.db.db import User
from app.initialize_functions import initialize_route, initialize_swagger
from app.db.config import initialize_db
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
from flask_login import LoginManager
from flask_httpauth import HTTPBasicAuth
# from dotenv import load_dotenv
# import os
# load_dotenv()

login_auth = LoginManager()
mail = Mail()


@login_auth.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()

# username = os.getenv('MAIL_USERNAME')
# password = os.getenv('MAIL_PASSWORD')
# server = os.getenv('MAIL_SERVER')
# tls = os.getenv('MAIL_USE_TLS')
# ssl = os.getenv('MAIL_USE_SSL')
# port = os.getenv('MAIL_PORT')

def create_app(config=None) -> Flask:
    """
    Create a Flask application.

    Args:
        config: The configuration object to use.

    Returns:
        A Flask application instance.
    """
    app = Flask(__name__)
    csrf = CSRFProtect(app)
    Bootstrap(app)
    auth = HTTPBasicAuth(app)
    login_auth.init_app(app)
    login_auth.session_protection = 'strong'
    login_auth.login_view = 'login_bp.login_valid_users'

    if config:
        app.config.from_object(get_config_by_name(config))

    # Flask-mail configuration
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] =  587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'jkimathi409@gmail.com'
    app.config['MAIL_PASSWORD'] ='yyasetywljzudphr'
    mail.init_app(app)

    # Initialize extensions
    initialize_db(app)

    # Register blueprints
    initialize_route(app)

    # Initialize Swagger
    initialize_swagger(app)

    return app, auth

# def send_email(subject, recipients, body):
#     try:
#         msg = Message(subject, recipients=recipients, sender='jkimathi409@gmail.com')
#         msg.body = body
#         mail.send(msg)
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email: {e}")
