from flask import Flask, request, render_template
import os

app = Flask(__name__)

picFolder = os.path.join('static','images')

app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/templates/search.html", methods = ["GET", "POST"])
def search():
    if request.method == "POST":
        common_benefits = request.form.get("benefit")
        occupation = request.form.get("occupation")
        interest =  request.form.get("interest")
        if(common_benefits == "Hotel and Travel Points"):
            return "This is a hotel boss"

        return "Your benefits are " + common_benefits + "\n" + "Your occupation is " + occupation + "\n" + "Your occupation is " + interest
    return render_template("search.html")

@app.route("/templates/profile.html")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run() 
