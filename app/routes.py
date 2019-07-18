from app import app
from flask import render_template, request
from app.models import model, formopener
import math

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    

@app.route('/encode', methods = ["GET","POST"])
def encode():
    userdata = dict(request.form)
    name = (userdata["message"])
    finalString = ""
    for l in range(0, len(name)):
        letter = int(ord(name[l]))
        pie = open("app/static/pie.txt").read()
        if pie[l] == ".":
            letter += 1
        else:
            letter += int(pie[l])
        finalString += chr(letter)
    return render_template('index.html', name = name, finalString = finalString)

@app.route('/decode', methods = ["GET","POST"])
def decrypt():
    if request.method == "GET":
        return render_template("decode.html")
    else:
        userdata = dict(request.form)
        name = (userdata["encoded_message"])
        finalString = ""
        for l in range(0, len(name)):
            letter = int(ord(name[l]))
            pie = open("app/static/pie.txt").read()
            if pie[l] == ".":
                letter -= 1
            else:
                letter -= int(pie[l])
            finalString += chr(letter)
    return render_template('decode.html', name = name, finalString = finalString)