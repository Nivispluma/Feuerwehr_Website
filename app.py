from flask import Flask, \
    render_template, \
    url_for, \
    request, \
    flash, \
    redirect, \
    session

import platform
from pathlib import Path
import os
import random

from forms import RegistrationForm, UserLogin

app = Flask(__name__)
app.config['SECRET_KEY'] = '6be7ec69776fa02df4c2970a3c197a35'

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


# -------------------------------------------------------------------------------

@app.route('/registrierung', methods=['GET', 'POST'])
@app.route('/Registrierung', methods=['GET', 'POST'])
def registration_page():  # put application's code here
    img_var_name = random.choice(os.listdir("static/styles/pictures/background/"))
    print(img_var_name)
    img_var_path = "styles/pictures/background/" + str(img_var_name)
    print(img_var_path)

    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        flash(f'Account wurde erstellt für {registration_form.username.data}', 'success')
        return redirect(url_for('index_page'))
    return render_template("registrierung.html", img_var_path=img_var_path, registration_form=registration_form)


@app.route('/login', methods=['GET', 'POST'])
@app.route('/Login', methods=['GET', 'POST'])
def login_page():  # put application's code here
    img_var_name = random.choice(os.listdir("static/styles/pictures/background/"))
    print(img_var_name)
    img_var_path = "styles/pictures/background/" + str(img_var_name)
    print(img_var_path)

    login_form = UserLogin()

    if login_form.validate_on_submit():
        flash(f'Wilkommen {login_form.user_email.data}', 'success')
        return redirect(url_for('index_page'))

    return render_template("login.html", img_var_path=img_var_path, login_form=login_form)


# -------------------------------------------------------------------------------------------

# run program


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
