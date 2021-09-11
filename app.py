from flask import Flask, request, render_template
import os

app = Flask(__name__)

picFolder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/templates/search.html")
def search():
    return render_template("search.html")

@app.route("/templates/profile.html")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run() 
