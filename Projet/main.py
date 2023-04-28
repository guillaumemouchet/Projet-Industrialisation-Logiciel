from flask import Flask, render_template, request, redirect, url_for, session
import string
import random
import datetime
# Project setup inspired from Flask workshop https://www.matthieuamiguet.ch/media/misc/flask2023/tuto/tuto.html
# Session setup: https://pythonbasics.org/flask-sessions/

app = Flask(__name__)
app.secret_key = 'secret'

# Taken from the special character and ambiguous list from Bitwarden
special_characters = '!@&$%^#\*'
confusing_characters = 'lIO10'

@app.get('/')
def hello():
    return render_template('home.html')

@app.get('/display_password')
def display_password():
    pwd = session.get('pwd')
    pwd_len = session.get('pwd_len') 
    is_readable =session.get('is_readable')
    return render_template("display_password.html", **locals())    

@app.post('/generate_password')
def generate_password():
    pwd_len = request.form['pwd_len']
    try:
        is_readable = request.form['is_readable'] 
    except:
        is_readable = False
    pwd = random_password(pwd_len, is_readable)
    session['pwd'] = pwd
    session['pwd_len'] = pwd_len
    session['is_readable'] = is_readable
    return redirect(url_for('display_password'))

#Inspiration https://www.geeksforgeeks.org/create-a-random-password-generator-using-python/
def random_password(pwd_len, is_readable):
    az = string.ascii_lowercase
    AZ = string.ascii_uppercase
    digits = string.digits

    if is_readable:
        #https://www.w3schools.com/python/ref_string_maketrans.asp
        translation_table = str.maketrans("","",confusing_characters)
        az = az.translate(translation_table)
        AZ = AZ.translate(translation_table)
        digits = digits.translate(translation_table)

    pwd = []
    #Making shure there is at least one of each
    pwd.append(random.choice(az))
    pwd.append(random.choice(AZ))
    pwd.append(random.choice(digits))
    pwd.append(random.choice(special_characters))

    char_list = az + AZ + digits + special_characters
    print(char_list)
    for i in range (int(pwd_len)-4):
        pwd.append(random.choice(char_list))
        
    random.shuffle(pwd)
    logPwd(pwd_len, is_readable)
    return "".join(pwd)

def logPwd(pwd_len, is_readable):
    f = open("log.txt", "a")
    now = datetime.datetime.now().strftime("%I:%M %d.%m.%Y")
    f.write(f"[{now}] {pwd_len} {is_readable}\n")
    f.close()
    
    