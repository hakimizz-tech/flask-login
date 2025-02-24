
from flask import Blueprint


signup_bp = Blueprint('signup_bp', __name__, template_folder='pages', static_folder='resources')

import app.modules.signup.view.signup