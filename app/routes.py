from app import app
from flask import render_template

@app.route('/')
def index():
    user= {'id': 1, 'username':'Patel', 'email':'keyurpatel1121@gmail.com'}
    return render_template('index.html', current_user=user)


@app.route('/test')
def test():
    return '**THIS IS A TEST**'
