import os
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return "About page"


@app.route("/cv")
def cv():
    return "CV page"


@app.route("/contact")
def contact():
    return "Contact page"




#TO RUN THIS
# python main.py
# -> Running on http://localhost:5000/

if __name__ == "__main__":
    from os import environ
    port = int(os.environ.get("PORT", 33507))
    app.run(debug=False, host='0.0.0.0', port=port)
