from flask import Flask, render_template, request, redirect, url_for, session
import string
import random
import datetime
import secrets
import requests
from flask_wtf import CSRFProtect

# Project setup inspired from Flask workshop https://www.matthieuamiguet.ch/media/misc/flask2023/tuto/tuto.html
# Session setup: https://pythonbasics.org/flask-sessions/

app = Flask(__name__)
csrf = CSRFProtect(app)
app.secret_key = "secret"

# Taken from the special character and ambiguous list from Bitwarden
special_characters = ["!", "@", "&", "$", "%", "^", "#", "*"]
confusing_characters = ["l", "I", "O", "1", "0"]


@app.get("/")
def hello():
    return render_template("home.html")


@app.get("/display_password")
def display_password():
  
    pwd = session.get("pwd")
    pwd_len = session.get("pwd_len")
    is_readable = session.get("is_readable")
    return render_template("display_password.html", **locals())


#@app.post("/generate_password")
@app.route("/generate_password", methods=['POST'])
def generate_password():
    pwd_len = request.form["pwd_len"]
    try:
        is_readable = request.form["is_readable"]
    except:
        is_readable = False
    pwd = random_password(pwd_len, is_readable)
    session["pwd"] = pwd
    session["pwd_len"] = pwd_len
    session["is_readable"] = is_readable
    return redirect(url_for("display_password"))


# Inspiration https://www.geeksforgeeks.org/create-a-random-password-generator-using-python/
def random_password(pwd_len, is_readable):
    try:
        pwd_len = int(pwd_len)
    except TypeError:
        raise TypeError("Please provide a valid integer")

    try:
        is_readable = bool(is_readable)
    except TypeError:
        raise TypeError("Please provide a valid bool")

    if pwd_len < 1:
        raise ValueError("Please enter an integer above 0")

    az = string.ascii_lowercase
    AZ = string.ascii_uppercase
    digits = string.digits

    if is_readable:
        # https://www.w3schools.com/python/ref_string_maketrans.asp
        translation_table = str.maketrans("", "", "".join(confusing_characters))
        az = az.translate(translation_table)
        AZ = AZ.translate(translation_table)
        digits = digits.translate(translation_table)

    pwd = []
    # Making shure there is at least one of each
    pwd.append(secrets.choice(az))
    pwd.append(secrets.choice(AZ))
    pwd.append(secrets.choice(digits))
    pwd.append(secrets.choice(special_characters))

    char_list = az + AZ + digits + "".join(special_characters)
    for i in range(int(pwd_len) - 4):
        pwd.append(secrets.choice(char_list))

    random.shuffle(pwd)
    log = generate_log(pwd_len, is_readable)
    logger_url = "http://127.0.0.1:8000/log"
    response = requests.post(logger_url, data={"log": log})
    if response.status_code != 200:
        print("Logging failed ", response.status_code)
    # logPwd(pwd_len, is_readable)

    return "".join(pwd)


def generate_log(pwd_len, is_readable):
    now = datetime.datetime.now().strftime("%I:%M %d.%m.%Y")
    log = f"[{now}] {pwd_len} {is_readable}\n"
    return log
