from flask import Blueprint


reset_password_bp = Blueprint('reset_password_bp', __name__, template_folder='pages', static_folder='resources')

import app.modules.reset_password.views.routes