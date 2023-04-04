from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")
    
@views.route('/percentCalc', methods=['GET', 'POST'])
def percent():
    return render_template("percCalc.html")
@views.route('/dotsCalc', methods=['GET', 'POST'])
def wilks():
    return render_template("dotsCalc.html")
