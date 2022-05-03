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


from forms import RegistrationForm, UserLogin

from flask_sqlalchemy import SQLAlchemy


# --------------------------- Config ----------------------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = '6be7ec69776fa02df4c2970a3c197a35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
fw_db = SQLAlchemy(app)  # create database instance

# ------------------------------------------------------------------------


class User(fw_db.Model):  # Defines the User Table
    id = fw_db.Column(fw_db.Integer, primary_key=True)
    username = fw_db.Column(fw_db.String(20), unique=True, nullable=False)
    user_email = fw_db.Column(fw_db.String(100), unique=True, nullable=False)
    profile_img = fw_db.Column(fw_db.String(20), nullable=False, default='default.jpg')
    password = fw_db.Column(fw_db.String(60), nullable=False)

    # defines the output of the Database
    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.user_email}','{self.profile_img}')"


# Hilfe gibt es durch den Guide
# https://www.youtube.com/watch?v=oYRda7UtuhA&t=524s


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
    # just some debugging BS
    if request.method == 'POST':
        print("Schmutz")
    print(registration_form.validate_on_submit())
    print(registration_form.errors)
    # ---------------------------------------------------

    if registration_form.validate_on_submit():
        flash(f'Account wurde erstellt für {registration_form.username.data}', 'success')
        return redirect(url_for('index_page'))

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
        # flash(f'Wilkommen {login_form.user_email.data}', 'success')
        print("Registration debug")
        return redirect(url_for("index_page"))

    return render_template("login.html", img_var_path=get_background_img_path(), login_form=login_form)


# ------------------------------- Searcher -----------------------------------------------------


@app.route('/wikiSearch', methods=['POST', 'GET'])
def wiki_search():
    return render_template("wikiSearch.html", img_var_path=get_background_img_path())


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
