from flask import Flask, render_template
# from flask_talisman import Talisman


app = Flask(__name__, static_url_path='/static')
# talisman = Talisman(app)

@app.route("/")
def index():
    return render_template("index.html", page="home")

@app.route("/research")
def research():
    return render_template("research.html", page="research")

@app.route("/teaching")
def teaching():
    return render_template("teaching.html", page="teaching")

@app.route("/writing")
def writing():
    return render_template("writing.html", page="writing")

# @app.route("/nudes")
# def nudes():
#     return render_template("contact.html", page="contact")

@app.route("/cv")
def cv():
    return render_template("cv.html", page="cv")

@app.route("/contact")
def contact():
    return render_template("contact.html", page="contact")





# TO RUN THIS
# python main.py
# -> Running on http://localhost:33507/

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 33507))
    app.run(debug=False, host="0.0.0.0", port=port)
