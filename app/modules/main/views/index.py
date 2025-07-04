from flask import abort, flash, make_response, render_template, request
from flask_login import login_required, current_user
from app.db.db import User
from app.modules.main import main_bp
from app.modules.main.form.home import HomeForm


@main_bp.route('/', methods=['GET', 'POST'])
@login_required
def home():
    form = HomeForm()
    if not current_user.is_authenticated:
        abort(404)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.objects(registration_number=form.search.data)
            if user is not None:
                return render_template('user.html', user=user)
            else:
                flash('student not found')
                return render_template('home.html')
    else:
        return make_response(render_template('home.html', form=form),200)
    
