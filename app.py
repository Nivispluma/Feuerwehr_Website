from flask import Flask, render_template
import platform
from pathlib import Path
import os, random


app = Flask(__name__)

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


# -------------------- Test Function --------------------

@app.route('/lab')
@app.route('/test')
def test_page():  # put application's code here
    img_var_name = random.choice(os.listdir("static/styles/pictures/background/"))
    print(img_var_name)
    img_var_path = "styles/pictures/background/" + str(img_var_name)
    print(img_var_path)

    return render_template("test.html", img_var_path=img_var_path)


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
    return render_template("gallery.html",images=images)





# run program
if __name__ == '__main__':
    app.run(debug=True)
