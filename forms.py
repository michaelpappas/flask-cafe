"""Forms for Flask Cafe."""

from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SelectField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length, URL

class CafeForm(FlaskForm):
    """ Form for adding a cafe. """

    name = StringField(
        "Name",
        validators=[
            InputRequired(),
            Length(max=30)
        ]
    )

    description = TextField(
        "Description",
    )

    url = StringField(
        "URL",
        validators=[URL()]
    )

    address = StringField(
        "Address",
        validators=[
            InputRequired(),
            Length(max=50)
        ]
    )

    city = SelectField(
        "city",
        coerce=int)

    image = StringField(
        "Image Url",
        validators=[URL()]
    )

