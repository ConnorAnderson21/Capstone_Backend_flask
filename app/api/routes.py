

from flask import Blueprint, render_template, request, json

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
        bmr = int(data.get('bmr'))
        activity_factor = data.get('activityFactor')
        carbohydrate = int(data.get('carbohydrate'))
        fat = int(data.get('fat'))
        protein = int(data.get('protein'))


        user = User.query.filter_by(email=email).first()
        if not user:
            
            user = User(
                username=username,
                email=email,
                height=height,
                weight=weight,
                age=age,
                gender=gender,
                bmr=bmr,
                activity_factor=activity_factor,
                carbohydrate=carbohydrate,
                fat=fat,
                protein=protein
                )
            db.session.add(user)
            db.session.commit()
        else:
            user.username = username
            user.height = height
            user.weight = weight
            user.age = age
            user.gender = gender
            user.bmr = bmr
            user.activity_factor = activity_factor

            print(bmr, activity_factor)
            user.calories = bmr * activity_factor
            user.carbohydrate = carbohydrate
            user.fat = fat 
            user.protein = protein
            db.session.commit()

        return {'message': 'Data submitted successfully!'}

    return {'message': 'Invalid request.'}


