from flask import render_template, Blueprint

aboutus=Blueprint('aboutus',__name__)

@aboutus.route('/aboutus')
def aboutus_home():
  return render_template('aboutus.html', title='aboutus')