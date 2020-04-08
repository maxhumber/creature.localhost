from flask import Flask, render_template
from flask_simplelogin import SimpleLogin, login_required
import config

app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = config.secret
SimpleLogin(app, login_checker=config.login_checker)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/page')
def creatures():
    return render_template("page.html")

@app.route('/table')
def table():
    return render_template("table.html")

@app.route('/protected')
@login_required()
def protected():
    return render_template("protected.html")

@app.route('/ocr')
def ocr():
    return render_template("ocr.html")

@app.route('/media')
def media():
    return render_template("media.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/mvp')
def mvp():
    return render_template("mvp.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
