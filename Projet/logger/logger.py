from flask import Flask, render_template, request, redirect, url_for, session
import string
import random
import datetime

# Project setup inspired from Flask workshop https://www.matthieuamiguet.ch/media/misc/flask2023/tuto/tuto.html


app = Flask(__name__)


@app.post("/log")
def log():
    logPwd(request.form.get("log"))
    return "Log successful"


def logPwd(log):
    f = open("log.txt", "a")
    now = datetime.datetime.now().strftime("%I:%M %d.%m.%Y")
    f.write(log)
    f.close()
