from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cv")
def cv():
    return "CV page"

#TO RUN THIS
# python main.py
# -> Running on http://localhost:5000/

if __name__ == "__main__":
    app.run()
