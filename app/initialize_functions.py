from app.modules.reset_password import reset_password_bp
from flask import Flask
from flasgger import Swagger
from app.modules.main import main_bp
from app.modules.signup import signup_bp
from app.modules.login import login_bp
# from app.db.db import db


def initialize_route(app: Flask):
    with app.app_context():
        app.register_blueprint(main_bp, url_prefix='')
        app.register_blueprint(signup_bp, url_prefix='')
        app.register_blueprint(login_bp, url_prefix='')
        app.register_blueprint(reset_password_bp, url_prefix='')



# def initialize_db(app: Flask):
#     with app.app_context():
#         db.init_app(app)
#         db.create_all()

def initialize_swagger(app: Flask):
    with app.app_context():
        swagger = Swagger(app)
        return swagger