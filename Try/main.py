from flask import render_template
from create_db import app, db, Meal_Name, Meal_Category, Meal_Area, Meal_Ingredients, Meal_Instructions, Meal_Image, create_meals

@app.route('/')
def index():
	return render_template('hello.html')
	
@app.route('/meals/')
def meals():
	meals = db.session.query(Meal_Name).all()
	return render_template('meals.html', meals = meals)
	
if __name__ == "__main__":
	app.run()
