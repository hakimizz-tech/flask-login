
from flask import Blueprint


main_bp = Blueprint('main_bp', __name__, template_folder='pages', static_folder='resources')

import app.modules.main.views.index