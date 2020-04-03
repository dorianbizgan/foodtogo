from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import traceback
from cache_meals import meals, find_meal
#<<<<<<< Updated upstream
from create_db import app, db, Meal_Name, Meal_Category, Meal_Area, Meal_Ingredients, Meal_Instructions, Meal_Image, create_meals
from sqlalchemy import func
from sqlalchemy import distinct
#=======
#from models import app, db, Meal_Name, Meal_Category, Meal_Area, Meal_Ingredients, Meal_Instructions, Meal_Image
#from flask_sqlalchemy import SQLAlchemy

#>>>>>>> Stashed changes

#adding break for HTML whenever there's a new line in instructions
#for meal in meals:
#	meal["strInstructions"] = meal["strInstructions"].replace('\n', '<br>')

#import sys
#if sys.version_info.major < 3:
#    reload(sys)
#sys.setdefaultencoding('utf8')

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
	meals = db.session.query(Meal_Name).all()
	return (render_template("meals.html", meals=meals))

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

	#### REMOVE EVENTUALLY
	meal = find_meal(meal_id)
	ingredients = []
	amounts = []
	combined = []
	#### REMOVE EVENTUALLY

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
	meal_instruction_temp = "Step 1:"
	step = 2
	active = False
	for ch in meal_instruction:
		if ch == ".":
			meal_instruction_temp += ". <br><br> Step " + str(step) + ": "
			step += 1
			continue
		meal_instruction_temp += ch
	meal_instruction = meal_instruction_temp[:-9]
	meal_instruction = meal_instruction.strip("\n").strip("\r")
	print(meal_temp[0])


	meal = {"strMeal": meal_temp[0].strip("[(u'").strip("','])"), "strInstructions":meal_instruction, "strMealThumb": meal_img, "strArea": meal_area, "strCategory": meal_category}
	#print(str(meal_temp[0]).strip("[(u'").strip("','])"))
	#print(type(meal_temp[0]))
#>>>>>>> Stashed changes

	for i in range(1,21):
		ingredient_num = "ingredient_" + str(i)
		measure_num = "measure_" + str(i)
		ingredient = db.session.query(getattr(Meal_Ingredients,ingredient_num)).filter(Meal_Ingredients.idMeal == int(meal_id)).all()
		'''<<<<<<< Updated upstream
		measure = db.session.query(getattr(Meal_Ingredients,measure_num)).filter(Meal_Ingredients.idMeal == int(meal_id)).all()
		#for j in ingredient:
		ingredient = str(ingredient[0]).strip("(u'").strip("',)")
		measure    = str(measure[0]).strip("(u'").strip("',)")
		if ingredient == "None" or ingredient == "":
			continue
		combined.append({"ingredient":ingredient,"measure":measure})
		=======
		'''
		measure = db.session.query(getattr(Meal_Ingredients,measure_num)).filter(Meal_Ingredients.idMeal == int(meal_id))
		#for j in ingredient:
		ingredient = str(ingredient[0]).strip("(u'").strip("',)")
		measure    = str(measure[0]).encode('utf-8').decode('unicode_escape').strip("(u'").strip("',)")
		if ingredient == "None" or ingredient == "":
			continue
		combined.append({"ingredient":ingredient,"measure":measure})
#>>>>>>> Stashed changes

		#print(str(ingredient)[0].strip("[(u'").strip("',)"))

	#	a = db.session.query(Meal_Ingredients.ingredient_num)
	#	b = db.session.query(Meal_)
	#for i in temp_ingredients:
	#	print(i)

	#temptemp = conn.execute(db.select("*").where(Meal_Ingredients.idMeal == int(meal_id)))
	#print(str(temptemp))
	'''
	for key in meal:
		if "strIngredient" in key and meal[key] != None and meal[key] != '':
			ingredients.append(meal[key])

		if "strMeasure" in key and meal[key] != None and meal[key] != '':
			amounts.append(meal[key])
<<<<<<< Updated upstream
			
=======

>>>>>>> Stashed changes
	#print(str(ingredients) +  "\n" + str(amounts))
	for i in ingredients:
		try:
			combined.append({"ingredient":i,"measure":amounts[ingredients.index(i)]})
		except:
			continue
	'''
#<<<<<<< Updated upstream
#=======
	for i in combined:
		print(i)
#>>>>>>> Stashed changes
	ingredients = combined
	return(render_template("show_meal.html", meal=meal, ingredients=ingredients))
		
if __name__ == '__main__':
#<<<<<<< Updated upstream
#	app.run()
#=======

	app.run(host = '0.0.0.0', port = 5000)
#>>>>>>> Stashed changes
	

