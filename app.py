from flask import Flask, \
    render_template, \
    url_for, \
    request, \
    flash, \
    redirect, \
    session

import wtforms
import platform
from pathlib import Path
import os
import random
import json

from helper import get_background_img_path

# for reverse proxy
import requests

# html Forms
from forms import RegistrationForm, UserLogin
# Database
from flask_sqlalchemy import SQLAlchemy
# Hashing
from flask_bcrypt import Bcrypt
# Login
from flask_login import LoginManager, UserMixin, login_user, user_logged_in

# --------------------------- Config and Init ----------------------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = '6be7ec69776fa02df4c2970a3c197a35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
fw_db = SQLAlchemy(app)  # create database instance
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


# ----------------

# Beispieluser
# testerino@besterino.com
# Alarma123
# d65f4sgt65!/")($/

# ----------------


# --------------------------- Database Stuff ---------------------------------------------


class User(fw_db.Model, UserMixin):  # Defines the User Table
    id = fw_db.Column(fw_db.Integer, primary_key=True)
    username = fw_db.Column(fw_db.String(20), unique=True, nullable=False)
    user_email = fw_db.Column(fw_db.String(100), unique=True, nullable=False)
    profile_img = fw_db.Column(fw_db.String(20), nullable=False, default='default.jpg')
    password = fw_db.Column(fw_db.String(60), nullable=False)

    # defines the output of the Database
    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.user_email}','{self.profile_img}')"

    # --------------------------------------------------


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --------------------------- Route Stuff ---------------------------------------------

@app.route('/')
@app.route('/home')
def index_page():  # put application's code here

    return render_template("index.html", img_var_path=get_background_img_path())


# -------------------- Emergency Selection Function --------------------

@app.route('/Einsatz_Auswahl')
def choose_emergency_operation():
    emergencies = os.listdir("static/styles/pictures/gallery")
    return render_template("choose_emergency.html",emergencies=emergencies)


# -------------------- Gallery Function --------------------

@app.route('/gallery')
@app.route('/Gallerie')
def gallery_page():
    images = os.listdir("static/styles/pictures/gallery/Einsatz 1")
    print(images)
    # also give render template the chosen emergency
    return render_template("gallery.html", images=images)

# --------------------------------------------------

# -------------------- Test Function --------------------


@app.route('/lab')
@app.route('/test')
def test_page():  # put application's code here

    return render_template("test.html", img_var_path=get_background_img_path())


# -------------------- Test Function --------------------


@app.route('/lab2')
@app.route('/test2')
def test_page_2():  # put application's code here

    return render_template("test2.html", img_var_path=get_background_img_path())


# -------------------- Test Function --------------------

@app.route('/canvas_test')
def canvas_page():  # put application's code here

    return render_template("canvas.html", img_var_path=get_background_img_path())


# -------------------------- Registrierung -----------------------------------------------------

@app.route('/registrierung', methods=['GET', 'POST'])
@app.route('/Registrierung', methods=['GET', 'POST'])
def registration_page():  # put application's code here

    registration_form = RegistrationForm()
    # ---------------------------------------------------

    if registration_form.validate_on_submit():
        print(registration_form.is_submitted())
        # ----------------- Database Stuff ----------------------------------
        # create hashed password from password form
        hashed_password = bcrypt.generate_password_hash(registration_form.password.data).decode('utf-8')
        # create Database entry
        user = User(username=registration_form.username.data, user_email=registration_form.user_email.data, password=hashed_password)
        # add and commit new User to the Database
        fw_db.session.add(user)
        fw_db.session.commit()
        # ---------------------------------------------------

        flash(f'Account wurde erstellt!', 'success')
        return redirect(url_for('login_page'))

    return render_template("registrierung.html", img_var_path=get_background_img_path(), registration_form=registration_form)


# -------------------------- Login -----------------------------------------------------

@app.route('/login', methods=['POST', 'GET'])
# @app.route('/Login', methods=['GET', 'POST'])
def login_page():  # put application's code here

    login_form = UserLogin()

    # ---------------------------------------------------
    # just some debugging BS
    if request.method == 'POST':
        print("Schmutz")
    print(login_form.validate_on_submit())
    print(login_form.errors)
    # ---------------------------------------------------

    if login_form.validate_on_submit():
        user = User.query.filter_by(user_email=login_form.user_email.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            flash(f'Wilkommen {login_form.user_email.data}', 'success')
            session["logged_in"] = True
            return redirect(url_for("index_page"))

        else:
            flash(f'Login fehlgeschlagen', 'failure')

    return render_template("login.html", img_var_path=get_background_img_path(), login_form=login_form)


# ------------------------------- Searcher -----------------------------------------------------


@app.route('/wikiSearch', methods=['POST', 'GET'])
def wiki_search():
    # check if user is logged in, if not redirect to login
    if "logged_in" in session:
        if session["logged_in"]:
            return render_template("wikiSearch.html", img_var_path=get_background_img_path())
        else:
            return redirect(url_for("login_page"))

    else:
        return redirect(url_for("login_page"))


# ------------------------------- Reverse Proxy ------------------------------------------------------------


@app.route('/proxy', methods=['POST', 'GET'])
def reverse_proxy():
    # get the url for wiki search
    url = request.args['url']
    # save the response from wikipedia
    response = requests.get(url)
    # convert the response to text and convert it json
    data = json.loads(response.text)
    # return a json
    return data

# ------------------------------- Error Handler ------------------------------------------------------------


# Error 404 - URL not found
@app.errorhandler(404)
def error_handler_page_404(e):
    return render_template("Error_Pages/err404.html"), 404


# Error 500 - Internal Server Error
@app.errorhandler(500)
def error_handler_page_500(e):
    return render_template("Error_Pages/err500.html"), 500

# -------------------------------------------------------------------------------
# run program


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
