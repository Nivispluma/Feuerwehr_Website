from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, length, email, equal_to
from flask_bcrypt import Bcrypt

class RegistrationForm(FlaskForm):
    # check if email exists in database

    def validate_user_email(self, user_email):
        from app import User
        print(user_email.data)
        mail = User.query.filter_by(user_email=user_email.data).first()
        print(f'daten: {User.query.all()}')
        print("validator debug email")
        print(mail)
        if mail:
            raise ValidationError('Diese Email existiert bereits')
        return



    def validate_username(self, username):
        from app import User
        print(f'want to create: {username.data}')
        user = User.query.filter_by(username=username.data).first()
        print(f'daten: {User.query.all()}')
        print("validator debug user")
        print(user)
        if user:
            raise ValidationError('Dieser Benutzername existiert bereits')
        return



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

    # ------------------------ custom Validator -------------------------

    # template
    # def validate_field(self, field):
    #   if True:
    #       raise ValidationError('Validation Message')

# -----------------------------------------------------------


class UserLogin(FlaskForm):
    # -----------------------------------------------------------

    # -----------------------------------------------------------

    user_email = StringField('Email',
                             validators=[DataRequired(), email()])

    password = PasswordField('Passwort',
                             validators=[DataRequired(),length(min=8)])

    stay_logged_in = BooleanField('merken')

    submit_button = SubmitField('Anmelden')


