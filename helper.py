import random
import os


def get_background_img_path():
    img_var_name = random.choice(os.listdir("static/styles/pictures/background/"))
    # print(img_var_name)
    img_var_path = "styles/pictures/background/" + str(img_var_name)
    # print(img_var_path)
    return img_var_path