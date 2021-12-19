from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "secretPassword"
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/hello")
def index():
    flash("Enter your name:")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Welcome " + str(request.form['name_input']) + ", to Run Club 2022!")
    return render_template("index.html")

