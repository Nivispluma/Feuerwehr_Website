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
    img_var_name = random.choice(os.listdir("static/styles/pictures/background/"))
    print(img_var_name)
    img_var_path = "styles/pictures/background/" + str(img_var_name)
    print(img_var_path)

    return render_template("index.html", img_var_path=img_var_path)


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
    img_var_name = random.choice(os.listdir("static/styles/pictures/background/"))
    print(img_var_name)
    img_var_path = "styles/pictures/background/" + str(img_var_name)
    print(img_var_path)

    return render_template("test.html", img_var_path=img_var_path)


# -------------------- Test Function --------------------


@app.route('/lab2')
@app.route('/test2')
def test_page_2():  # put application's code here
    img_var_name = random.choice(os.listdir("static/styles/pictures/background/"))
    print(img_var_name)
    img_var_path = "styles/pictures/background/" + str(img_var_name)
    print(img_var_path)

    return render_template("test2.html", img_var_path=img_var_path)


# -------------------- Test Function --------------------

@app.route('/canvas_test')
def canvas_page():  # put application's code here
    img_var_name = random.choice(os.listdir("static/styles/pictures/background/"))
    print(img_var_name)
    img_var_path = "styles/pictures/background/" + str(img_var_name)
    print(img_var_path)

    return render_template("canvas.html", img_var_path=img_var_path)


# -------------------------- Registrierung -----------------------------------------------------

@app.route('/registrierung', methods=['GET', 'POST'])
@app.route('/Registrierung', methods=['GET', 'POST'])
def registration_page():  # put application's code here
    img_var_name = random.choice(os.listdir("static/styles/pictures/background/"))
    print(img_var_name)
    img_var_path = "styles/pictures/background/" + str(img_var_name)
    print(img_var_path)

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

    return render_template("registrierung.html", img_var_path=img_var_path, registration_form=registration_form)


# -------------------------- Login -----------------------------------------------------

@app.route('/login', methods=['POST', 'GET'])
# @app.route('/Login', methods=['GET', 'POST'])
def login_page():  # put application's code here
    img_var_name = random.choice(os.listdir("static/styles/pictures/background/"))
    print(img_var_name)
    img_var_path = "styles/pictures/background/" + str(img_var_name)
    print(img_var_path)

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

    return render_template("login.html", img_var_path=img_var_path, login_form=login_form)

# ------------------------------- Reverse Proxy ------------------------------------------------------------


@app.route('/proxy', methods=['POST', 'GET'])
def reverse_proxy():
    api_key = "39c7b6d066d8513e8ce2a535a143f4f6"

    url_2 = request.args['url']
    print(url_2)

    lat = "48.208176"
    lon = "16.373819"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)
    #url_2 = "https://en.wikipedia.org/w/api.php?action=query&format=json&revids=347819%7C5487%7C548945&formatversion=2"

    response = requests.get(url)
    data = json.loads(response.text)
    #print(data)

    response_2 = requests.get(url_2)
    data_2 = json.loads(response_2.text)
    print(data_2)

    return data_2


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
