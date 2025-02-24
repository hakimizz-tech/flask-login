
from flask import flash, redirect, request, url_for, make_response, render_template
from flask_login import login_required, login_user, logout_user
from app.db.db import User
from app.modules.login import login_bp
from app.modules.login.form.login import LoginForm
from flask_bcrypt import Bcrypt
from app.modules.login.repository.login import LoginRepository

@login_bp.route('/login', methods=['POST', 'GET'])
def login_valid_users():
    bcrypt = Bcrypt()
    form = LoginForm()
    repo = LoginRepository()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = repo.get_login_email(form.email.data)
            if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash('Login successful', 'success')
                return redirect(url_for('main_bp.home'))
            else:
                # handle invalid login attempt
                flash('Login Unsuccessful. Please use a valid email and password', 'error')
                return make_response(render_template('login.html', form=form), 200)
            
    # GET method
    else:
        return make_response(render_template('login.html', form=form),200)

@login_bp.get('/logout')    
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_bp.home'))