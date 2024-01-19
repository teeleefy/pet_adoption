"""Forms for our Flask app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, URLField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    age = FloatField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    species = SelectField("Species", choices=['cat', 'dog', 'porcupine'], validators=[InputRequired()])
    photo_url = URLField('Photo URL', validators=[Optional()])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Available')

