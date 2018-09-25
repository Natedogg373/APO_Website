"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

@app.route('/')
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/howtojoin')
def howtojoin():
    return render_template('howtojoin.html')

@app.route('/Upcomingevents')
def Upcomingevents():
    return render_template('Upcomingevents.html')

@app.route('/meetourexect')
def meetourexec():
    return render_template('meetourexec.html')


if __name__== '__main__':
        app.run(debug=True)