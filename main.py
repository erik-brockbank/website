import os
from flask import Flask, render_template
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def index():
    return render_template("index.html", page="home")


@app.route("/about")
def about():
    return render_template("index.html", page="about")


@app.route("/cv")
def cv():
    return render_template("index.html", page="cv")


@app.route("/contact")
def contact():
    return render_template("index.html", page="contact")




#TO RUN THIS
# python main.py
# -> Running on http://localhost:5000/

if __name__ == "__main__":
    from os import environ
    port = int(os.environ.get("PORT", 33507))
    app.run(debug=False, host='0.0.0.0', port=port)
