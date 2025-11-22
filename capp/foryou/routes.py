from flask import Blueprint, render_template

foryou = Blueprint('foryou', __name__, template_folder='templates')

@foryou.route('/foryou')
def foryou_home():
    return render_template('foryou.html')
