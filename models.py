# beginning of models.py
# note that at this point you should have created "mealdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://dorianbizgan:asd123@localhost:5432/mealsdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

class Meal_Name(db.Model):
    
	__tablename__ = 'meal_name'
	meal_name = db.Column(db.String(80), nullable = False)
	idMeal = db.Column(db.Integer, primary_key=True)


class Meal_Category(db.Model):

	__tablename__ = 'meal_category'
	idMeal = db.Column(db.Integer, primary_key = True)
	category = db.Column(db.String(80), nullable = False)

class Meal_Area(db.Model):
        
	__tablename__ = 'meal_area'
	idMeal = db.Column(db.Integer, primary_key = True)
	area = db.Column(db.String(80), nullable = False)

class Meal_Ingredients(db.Model):
        
	__tablename__ = 'meal_ingredients'
	idMeal = db.Column(db.Integer, primary_key = True)
	ingredient_1 = db.Column(db.String(80), nullable = True)
	ingredient_2 = db.Column(db.String(80), nullable = True)
	ingredient_3 = db.Column(db.String(80), nullable = True)
	ingredient_4 = db.Column(db.String(80), nullable = True)
	ingredient_5 = db.Column(db.String(80), nullable = True)
	ingredient_6 = db.Column(db.String(80), nullable = True)
	ingredient_7 = db.Column(db.String(80), nullable = True)
	ingredient_8 = db.Column(db.String(80), nullable = True)
	ingredient_9 = db.Column(db.String(80), nullable = True)
	ingredient_10 = db.Column(db.String(80), nullable = True)
	ingredient_11 = db.Column(db.String(80), nullable = True)
	ingredient_12= db.Column(db.String(80), nullable = True)
	ingredient_13 = db.Column(db.String(80), nullable = True)
	ingredient_14 = db.Column(db.String(80), nullable = True)
	ingredient_15 = db.Column(db.String(80), nullable = True)
	ingredient_16 = db.Column(db.String(80), nullable = True)
	ingredient_17 = db.Column(db.String(80), nullable = True)
	ingredient_18 = db.Column(db.String(80), nullable = True)
	ingredient_19 = db.Column(db.String(80), nullable = True)
	ingredient_20 = db.Column(db.String(80), nullable = True)
	#base = 'ingredient_'
	#for i in range(1,21):
            #globals()[base + str(i)] = db.Column(db.String(80), nullable = True)

	measure_1 = db.Column(db.String(80), nullable = True)
	measure_2 = db.Column(db.String(80), nullable = True)
	measure_3 = db.Column(db.String(80), nullable = True)
	measure_4 = db.Column(db.String(80), nullable = True)
	measure_5 = db.Column(db.String(80), nullable = True)
	measure_6 = db.Column(db.String(80), nullable = True)
	measure_7 = db.Column(db.String(80), nullable = True)
	measure_8 = db.Column(db.String(80), nullable = True)
	measure_9 = db.Column(db.String(80), nullable = True)
	measure_10 = db.Column(db.String(80), nullable = True)
	measure_11 = db.Column(db.String(80), nullable = True)
	measure_12 = db.Column(db.String(80), nullable = True)
	measure_13 = db.Column(db.String(80), nullable = True)
	measure_14 = db.Column(db.String(80), nullable = True)
	measure_15 = db.Column(db.String(80), nullable = True)
	measure_16 = db.Column(db.String(80), nullable = True)
	measure_17 = db.Column(db.String(80), nullable = True)
	measure_18 = db.Column(db.String(80), nullable = True)
	measure_19 = db.Column(db.String(80), nullable = True)
	measure_20 = db.Column(db.String(80), nullable = True)
	
	#base = 'measure_'
	#for i in range(1,21):
            #globals()[base + str(i)] = db.Column(db.String(80), nullable = True)

class Meal_Instructions(db.Model):
        
	__tablename__ = 'meal_instructions'
	idMeal = db.Column(db.Integer, primary_key = True)
	instructions = db.Column(db.VARCHAR(5000), nullable = False)

class Meal_Image(db.Model):
        
	__tablename__ = 'meal_image'
	idMeal = db.Column(db.Integer, primary_key = True)
	image = db.Column(db.VARCHAR(100), nullable = False)


db.create_all()
# End of models.py
