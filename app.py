from flask import Flask , render_template 
app = Flask(__name__)

@app.route("/")
def index():
    heading ="This is the first Variable by Python Variabels"
    return render_template("index.html", heading = heading)
