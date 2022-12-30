"""Forms for Flask Cafe."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, EmailField, TextAreaField
from wtforms.validators import InputRequired, Length, URL, Optional

class CafeForm(FlaskForm):
    """ Form for adding a cafe. """

    name = StringField(
        "Name",
        validators=[
            InputRequired(),
            Length(max=30)
        ]
    )

    description = TextAreaField(
        "Description",
    )

    url = StringField(
        "URL",
        validators=[URL(), Optional()]
    )

    address = StringField(
        "Address",
        validators=[
            InputRequired(),
            Length(max=50)
        ]
    )

    city = SelectField(
        "City")

    image = StringField(
        "Image Url",
        validators=[URL(), Optional()]
    )

class SignupForm(FlaskForm):
    """ Form for adding a new user. """

    username = StringField("Username",
                validators=[
                    InputRequired(),
                    Length(max=30)
                ]
    )

    first_name = StringField("First Name",
                validators=[
                    InputRequired(),
                    Length(max=30)
                ]
    )

    last_name = StringField("Last Name",
                valididators=[
                    InputRequired(),
                    Length(max=30)
                ]
    )

    description = TextAreaField("Description",
    )

    email = EmailField("Email",
            validators=[InputRequired()]
            )

    password = PasswordField("Password",
                validators=[Length(min=6)]
    )

    image_url = StringField("Image URL",
                validators=[URL(), Optional()]
                )

class LoginForm(FlaskForm):
    """ Form for logging in. """

    username = StringField("Username",
                validators=[InputRequired()]
    )

    password = PasswordField("Password",
                validators=[InputRequired()]
    )

class LoginForm(FlaskForm):
    """ Form for adding a new user. """

    username = StringField("Username",
                validators=[
                    InputRequired(),
                    Length(max=30)
                ]
    )

    password = PasswordField("Password",
                validators=[Length(min=6)]
    )
