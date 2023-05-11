from flask import Flask, request


# Project setup inspired from Flask workshop https://www.matthieuamiguet.ch/media/misc/flask2023/tuto/tuto.html

app = Flask(__name__)


@app.post("/log")
def log():
    log_pwd(request.form.get("log"))
    return "Log successful"


def log_pwd(log):
    f = open("log.txt", "a")
    f.write(log)
    f.close()
