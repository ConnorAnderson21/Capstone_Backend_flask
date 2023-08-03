

from flask import Blueprint, render_template, request, jsonify, json

from ..models import User, db

api = Blueprint('api', __name__, url_prefix='/api')

# https://api.edamam.com/api/food-database/v2/parser?app_id=4ce8395f&app_key=50ba68fb629700b9d063ed7d7713bc0d&nutrition-type=logging


@api.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        height = int(data.get('heightInches'))
        weight = int(data.get('weightPounds'))
        age = int(data.get('age'))
        gender = data.get('gender')

        
        user = User.query.filter_by(email=email).first()
        if not user:
            
            user = User(
                username=username,
                email=email,
                height=height,
                weight=weight,
                age=age,
                gender=gender,
                calories=0,
                carbohydrate=0,
                fat=0,
                protein=0
            )
            db.session.add(user)
            db.session.commit()
        else:
            user.username = username
            user.height = height
            user.weight = weight
            user.age = age
            user.gender = gender
            db.session.commit()

        return {'message': 'Data submitted successfully!'}

    return {'message': 'Invalid request.'}


