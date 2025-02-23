from flask import Blueprint, render_template

# Create the Blueprint object with 'homepage' as the name
homepage = Blueprint("homepage", __name__, template_folder="templates")

# Define the default route for the homepage
@homepage.route("/")
def home():
    return render_template("homepage.html")

# Define the about route
@homepage.route("/about")
def about():
    return render_template("about.html")
