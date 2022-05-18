import logging
from flask import Flask, render_template, request, redirect
from models.forms import StatementForm
from controllers.addinput import tx_hash
from controllers.getnotice import notice

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config["DEBUG"] = True
app.logger.setLevel(logging.INFO)

def hex2str(hex):
    return bytes.fromhex(hex[2:]).decode("utf-8")

def str2hex(str):
    return "0x" + str.encode("utf-8").hex()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/addinput', methods=['GET', 'POST'])
def addinput():
    form = StatementForm()
    if request.method == "POST":
        statement = str2hex(request.form.get("statement"))
        print("Hex Statement:", statement)
        tx_hash(statement)
    return render_template('addinput.html', form=form)

@app.route('/getnot', methods=['GET', 'POST'])
def getnot():
    form = StatementForm()
    payload = None
    if request.method == "POST":
        epoch = request.form.get("epoch")
        payload = hex2str(notice(epoch))
        print(payload)
    return render_template('getnotice.html', form=form, payload=payload)