from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import traceback
import requests
from cache_meals import meals, find_meal
from create_db import app, db, Meal_Name, Meal_Category, Meal_Area, Meal_Ingredients, Meal_Instructions, Meal_Image, create_meals
from sqlalchemy import func
from sqlalchemy import distinct

global_c = ""
@app.route('/')
def home():
	return render_template("index.html")

@app.route('/about-us/')
def aboutUs():
	return (render_template("aboutUs.html"))

@app.route('/categories/')
def categories():
	categories  = db.session.query(distinct(Meal_Category.category))
	return (render_template("categories.html", categories = categories))


@app.route('/meals/')
def meals():
	#<<<<<<< HEAD
	#meals = db.session.query(Meal_Name).all()
	#return (render_template("meals.html", meals=meals))
	#=======
    arg = request.args
    page = request.args.get('page', 1, type = int)
    meals = db.session.query(Meal_Name).paginate(page = page, per_page =10)
    return (render_template("meals.html", meals=meals))
	#>>>>>>> f0c2f4a3dee7b2c2921b1d56b6678e84f66891a3

@app.route('/meals/country/<string:country>/')
def meals_country(country):
    global_c = country
    page = request.args.get('page', 1, type = int)
    meals = db.session.query(Meal_Name).filter_by(area = global_c).paginate(page = page, per_page = 10)
    return (render_template("meal_country.html", meals=meals, global_c= global_c))


@app.route('/countries/')
def countries():
	countries = db.session.query(distinct(Meal_Area.area))
	return (render_template("countries.html", countries = countries))

@app.route('/test/<int:meal_id>')
def test(meal_id):
	meal_temp = db.session.query(Meal_Name.meal_name).filter(Meal_Name.idMeal == int(meal_id)).all()[0]

	meal_img  = db.session.query(Meal_Image.image).filter(Meal_Image.idMeal == int(meal_id)).all()[0]
	meal_img = meal_img[0].encode('utf-8').decode('unicode_escape')

	meal_instr= db.session.query(Meal_Instructions.instructions).filter(Meal_Instructions.idMeal == int(meal_id)).all()[0]
	meal_instr= meal_instr[0].encode('utf-8').decode('utf-8')
	print(meal_temp)

	meal_temp = {"strMeal":meal_temp[0].encode(), "strMealThumb":meal_img, "strInstructions":meal_instr}
	return(render_template("show_meal.html", meal=meal_temp, ingredients=[]))

@app.route('/meals/<int:meal_id>')
def show_meal(meal_id):
	combined = []

	# Querying for the data from the database and converting to usable
	meal_temp = db.session.query(Meal_Name.meal_name).filter(Meal_Name.idMeal == int(meal_id)).all()[0]
	
	meal_instruction = db.session.query(Meal_Instructions.instructions).filter(Meal_Instructions.idMeal == int(meal_id)).all()[0]
	meal_instruction = str(meal_instruction[0].encode('utf-8').decode('utf-8'))
	
	meal_img  = db.session.query(Meal_Image.image).filter(Meal_Image.idMeal == int(meal_id)).all()[0]
	meal_img  = meal_img[0].encode('utf-8').decode('unicode_escape')

	meal_area  = db.session.query(Meal_Area.area).filter(Meal_Area.idMeal == int(meal_id)).all()[0]
	meal_area  = meal_area[0].encode('utf-8').decode('unicode_escape')

	meal_category  = db.session.query(Meal_Category.category).filter(Meal_Category.idMeal == int(meal_id)).all()[0]
	meal_category  = meal_category[0].encode('utf-8').decode('unicode_escape')



	# Programatically adding steps for easier reading
	meal_instruction_temp = "Step 1: "
	step = 2
	active = False
	for a,b in zip(meal_instruction, meal_instruction[1:]):
		print(a,b)
		if b == None:
			meal_instruction += a
			break
		if active == True:
			meal_instruction_temp += " <br><br> Step " + str(step) + ": " 
			step += 1
			a = b
			active = False
			continue
		try:
			int(a)
			if b == ".":
				active = True
				continue
			meal_instruction_temp += a

		except:
			meal_instruction_temp += a
			continue

	meal_instruction = meal_instruction_temp + b#[:-9]
	meal_instruction = meal_instruction.strip("\n").strip("\r")
	print(meal_temp[0])

	# add all of the queried data into format for Jinja template
	meal = {"strMeal": meal_temp[0].strip("[(u'").strip("','])"), "strInstructions":meal_instruction, "strMealThumb": meal_img, "strArea": meal_area, "strCategory": meal_category}

	for i in range(1,21):
		ingredient_num = "ingredient_" + str(i)
		measure_num = "measure_" + str(i)
		ingredient = db.session.query(getattr(Meal_Ingredients,ingredient_num)).filter(Meal_Ingredients.idMeal == int(meal_id)).all()

		measure = db.session.query(getattr(Meal_Ingredients,measure_num)).filter(Meal_Ingredients.idMeal == int(meal_id))
		#for j in ingredient:
		ingredient = str(ingredient[0]).strip("(u'").strip("',)")
		measure    = str(measure[0]).encode('utf-8').decode('utf-8').strip("(u'").strip("',)")
		if ingredient == "None" or ingredient == "":
			continue
		combined.append({"ingredient":ingredient,"measure":measure})

	for i in combined:
		print(i)

	ingredients = combined
	return(render_template("show_meal.html", meal=meal, ingredients=ingredients))
		
if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 5000)

