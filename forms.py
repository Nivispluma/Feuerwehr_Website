from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, email, equal_to


class RegistrationForm(FlaskForm):
    # varname = FieldType('html_label', validators=[Validator_Function()])
    username = StringField('Benutzername',
                           validators=[DataRequired(), length(min=2, max=20)])

    user_email = StringField('Email',
                             validators=[DataRequired(), email()])

    password = PasswordField('Passwort',
                             validators=[DataRequired(), length(min=8)])

    confirm_password = PasswordField('Passwort',
                                    validators=[DataRequired(), equal_to('password')])

    submit_button = SubmitField('Registrieren')

# -----------------------------------------------------------


class UserLogin(FlaskForm):
    user_email = StringField('Email',
                             validators=[DataRequired(), email()])

    password = PasswordField('Passwort',
                             validators=[DataRequired(), length(min=8)])

    stay_logged_in = BooleanField('merken')

    submit_button = SubmitField('Anmelden')


