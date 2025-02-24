from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user
from flask_mail import Message
from app.db.db import User
from app.modules.reset_password import reset_password_bp
from app.modules.reset_password.form.reset import RequestResetForm, ResetPasswordForm
from flask_bcrypt import Bcrypt
from app.modules.reset_password.repository.reset import ResetRepository


def send_reset_email(user):
    from app.app import mail
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('reset_password_bp.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


@reset_password_bp.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    repo = ResetRepository()
    form = RequestResetForm()
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))
    
    if request.method == 'POST':
        if form.validate_on_submit():
            user = repo.get_user_by_email(form.email.data)
            send_reset_email(user)
            flash('An email has been sent with instructions to reset your password.', 'info')
            return redirect(url_for('login_bp.login_valid_users'))
    else:
        return render_template('reset_request.html', title='Reset Password', form=form)


@reset_password_bp.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    bcrypt = Bcrypt()
    repo = ResetRepository()
    form = ResetPasswordForm()
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))
    user = User.verify_reset_token(token)

    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_password_bp.reset_request'))
    
    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            repo.update_user_password(user.id, hashed_password)
            
            flash('Your password has been updated! You are now able to log in', 'success')
            return redirect(url_for('login_bp.login_valid_users'))
    else:
        return render_template('reset_token.html', title='Reset Password', form=form)