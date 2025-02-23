from flask import Blueprint, render_template

# Define Blueprint
homepage = Blueprint('homepage', __name__, template_folder='templates')

# Routes
@homepage.route('/')
def home():
    return render_template('homepage.html')

@homepage.route('/about')
def about():
    return render_template('about.html')
