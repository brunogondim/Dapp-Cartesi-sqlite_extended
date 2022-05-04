import logging
from flask import Flask, render_template, request
from models.forms import StatementForm
from controllers.addinput import tx_hash
from controllers.connection import str_to_eth_hex

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config["DEBUG"] = True
app.logger.setLevel(logging.INFO)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = StatementForm()
    #if form.validate_on_submit():
    #   app.logger.info(f"Statement: {form.statement.data}")
    #else:
    #    app.logger.error(f"Error on Validation Form: {form.errors}")
    if request.method == "POST":
        statement = str_to_eth_hex(request.form.get("statement"))
        print("Hex Statement:", statement)
        tx_hash(statement)
    return render_template('form.html', form=form)