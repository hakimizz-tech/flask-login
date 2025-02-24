
from app.modules.signup import signup_bp
from app.modules.signup.form.signup import SignupForm
from app.db.db import User
from flask import abort, make_response, render_template, request, url_for, redirect
from app.modules.signup.repository.signup import SignupRepository
# from flask_security.utils import hash_password
from flask_bcrypt import Bcrypt

@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    bcrypt = Bcrypt()
    form = SignupForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            repo = SignupRepository()
            details = dict()
            details['first_name'] = form.first_name.data
            details['last_name'] = form.last_name.data
            details['email'] = form.email.data
            details['registration_number'] = form.registration_number.data
            details['mobile_number'] = form.mobile_number.data
            details['address'] = form.address.data
    
            # hash the password
            details['password'] = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            
            result = repo.insert_user(details)
            if result:
                return redirect(url_for('login_bp.login_valid_users'))
            else:
                abort(400)
    
    else:
        return make_response(render_template('signup.html', form=form), 200)

