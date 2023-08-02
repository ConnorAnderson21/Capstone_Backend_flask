from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    calories = db.Column(db.Integer)
    carbohydrate = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    protein = db.Column(db.Integer)

    def __init__(self, username, email, height, weight, age, gender, calories, carbohydrate, fat, protein):
        self.username=username
        self.email=email
        self.height=height
        self.weight=weight
        self.age=age
        self.gender=gender
        self.calories=calories
        self.carbohydrate=carbohydrate
        self.fat=fat
        self.protein=protein