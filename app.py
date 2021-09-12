import re
from flask import Flask, request, render_template
import os

app = Flask(__name__)

#creates folder of images from /static/images directory
picFolder = os.path.join('static','images')
#lets picFolder variable contain images
app.config['UPLOAD_FOLDER'] = picFolder

card1 = [1, 'Hotel & Travel Points', 'Student', 'User Rated 5/5', 'Chase Sapphire Preferred Card', 300, 629]
card2 = [2, 'Cash Back', 'Student', 'Low/No Annual Fee', 'Wells Fargo Active Cash Card', 630, 689]
card3 = [3, 'Cash Back', 'Student', 'High Reward Rate', 'Citi Custom Cash Card', 630, 689]
card4 = [4, 'Gas Points', 'Student', 'High Reward Rate', 'Blue Cash Preferred Cash from American Express', 690, 719]
card5 = [5, 'Hotel & Travel Points', 'Business', 'Low/No Annual Fee', 'Chase Freedom Unlimited', 720, 850]
card6 = [6, 'Retail Rewards', 'Business', 'High Reward Rate', 'Citi Double Cash Card', 690, 719]
card7 = [7, 'Low Interest', 'Business', 'User Rated 5/5', 'Discover it Cash Back', 630, 689]
card8 = [8, 'Retal Rewards', 'Business', 'Low/No Annual Fee', 'Capital One Venture Rewards Credit Card', 300, 629]
card9 = [9, 'Balance Transfer', 'Student', 'High Reward Rate', 'Capital One SavorOne Cash Rewards Credit Card', 630, 689]
card10 = [10, 'Airline Miles', 'Business', 'User Rated 5/5', 'U.S. Bank Altitude Connect Visa Signature Card', 720, 850]

cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10]

#Home Directory Path
@app.route("/")
def home():
    #Create profile_picture variable from profile.jpg
    profile_picture = os.path.join(app.config['UPLOAD_FOLDER'], 'profile.jpg')
    
    # return render_template("form.html", profile_image = profile_picture)
    message="Hello World"
    return render_template("form.html", message=message, profile_picture=profile_picture)
    

@app.route("/templates/search.html", methods = ["GET", "POST"])
def search():
    if request.method == "POST":
        common_benefits = request.form.get("benefit")
        occupation = request.form.get("occupation")
        other =  request.form.get("other")
        credit_score = 730

        for card in cards:
            if (card[2] == common_benefits or card[3] == occupation or card[4] == other) and (credit_score >= card[6] and credit_score <= card[7]):
                return "PLz complete this if statement"
        return "Your benefits are " + common_benefits + "\n" + "Your occupation is " + occupation + "\n" + "Your occupation is " + other
    return render_template("search.html")

@app.route("/templates/profile.html")
def profile():
    return render_template("profile.html")

@app.route("/templates/chart_testing.html")
def chart_testing():
    return render_template("chart_testing.html")



if __name__ == "__main__":
    app.run() 
