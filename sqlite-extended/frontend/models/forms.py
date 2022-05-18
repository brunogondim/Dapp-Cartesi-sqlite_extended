from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired


class StatementForm(FlaskForm):
    statement = StringField("Statement", validators=[DataRequired()])
    epoch = IntegerField("Epoch", validators=[DataRequired()])