

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class HomeForm(FlaskForm):
    search = StringField('Search user', validators=[DataRequired()])
    submit = SubmitField('submit', validators=[DataRequired()])