import re
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

@app.route("/templates/cards_images.html")
def cards_images():
    #first_name = request.form.get("fname")
    #last_name = request.form.get("lname")
    #credit_score = request.form.get("creditsore")
    photo_file = os.path.join(app.config['UPLOAD_FOLDER'], 'chase_sapphire_preferred.jpg','discover_it_secured','citi_double_cash_card')
    return render_template("cards_images.html", user_image = photo_file)

if __name__ == "__main__":
    app.run() 
