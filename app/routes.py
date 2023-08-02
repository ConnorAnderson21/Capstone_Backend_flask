from app import app

from flask import render_template


# https://api.edamam.com/api/food-database/v2/parser?app_id=4ce8395f&app_key=50ba68fb629700b9d063ed7d7713bc0d&nutrition-type=logging



@app.route('/')
def land():
    return render_template('index.html')

@app.route('/home')
def home():
    return {
        'Welcome home': 'there is no place like here'
    }

@app.route('/test')
def test():
    return {
        'Is this mic on?': 'is this function working????'
    }

