from app import app
from flask import render_template, request
from app.models import model, formopener, cypher
# from templates import index

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
# @app.routes('/encode')
# def encode():
#     return render_template("index.html" ,name = name)
    
@app.route('/encode', methods = ["GET","POST"])
def encode():
    if request.method == "GET":
        return "Please use the form"
    else:
        userdata = dict(request.form)
        print(userdata)
        # vre = userdata["breakfast"]
        name = userdata["message"]
        # breakfast = model.shout(vre.decode("utf-8"))
        # return "under contruction"
        return render_template('index.html', name = name)
        
# @app.route('/encoded')
# def encoded():
#     return