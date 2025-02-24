from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, Regexp, ValidationError
from app.db.db import User  # Import your User model

# Custom validators
def unique_email(form, field):
    if User.objects(email=field.data).first():
        raise ValidationError("Email already registered")

def unique_registration(form, field):
    if User.objects(registration_number=field.data).first():
        raise ValidationError("Registration number already in use")

def unique_mobile(form, field):
    if User.objects(mobile_number=field.data).first():
        raise ValidationError("Mobile number already in use")

class SignupForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('last name', validators=[DataRequired()])
    email = StringField(
        'email',
        validators=[DataRequired(), Email(), unique_email]
    )
    registration_number = StringField(
        'registration number',
        validators=[
            DataRequired(),
            Regexp(r'^[A-Za-z0-9]{6,12}$', message="Invalid registration number"),
            unique_registration
        ]
    )
    mobile_number = StringField(
        'mobile number',
        validators=[
            DataRequired(),
            Regexp(r'^\+?[0-9]{10,15}$', message="Invalid mobile number"),
            unique_mobile
        ]
    )
    address = StringField(
        'address',
        validators=[
            DataRequired(),
            Length(min=5, max=100, message="Address must be between 5 and 100 characters")
        ]
    )
    password = PasswordField(
        'password',
        validators=[
            DataRequired(),
            Length(min=8, message="Password must be at least 8 characters"),
            Regexp(
                r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
                message="Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character"
            )
        ]
    )