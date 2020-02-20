from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import traceback
from cache_meals import meals, find_meal
app = Flask(__name__)


#with open('cache_meals.txt','r') as inf:
#    dict_from_file = eval(inf.read())

@app.route('/')
def home():
    return render_template("bootstrap.html")

@app.route('/about-us/')
def aboutUs():
    return (render_template("aboutUs.html"))

@app.route('/ingredients/')
def ingredients():
    return (render_template("ingredients.html"))

@app.route('/meals/')
def meals():
    return (render_template("meals.html", meals=meals))

@app.route('/countries/')
def countries():
    return (render_template("countries.html"))

@app.route('/ingredients/<string:ingredient_filter>')
def meal_filtered(ingredient_filter):
	if ingredient_filter == "Free-range eggs":
		return(render_template("eggs.html"))
	if ingredient_filter == "almond extract":
		return(render_template("almonds.html"))
	if ingredient_filter == "butter":
		return(render_template("butter.html"))		

@app.route('/view/<int:meal_id>')
def show_meal(meal_id):
	meal = find_meal(meal_id)
	ingredients = []
	amounts = []
	combined = []

	for key in meal:
		if "strIngredient" in key and meal[key] != None and meal[key] != '':
			ingredients.append(meal[key])

		if "strMeasure" in key and meal[key] != None and meal[key] != '':
			amounts.append(meal[key])

	print(str(ingredients) +  "\n" + str(amounts))
	for i in ingredients:
		try:
			combined.append({"ingredient":i,"amount":amounts[ingredients.index(i)]})
		except:
			continue
	ingredients = combined
	return(render_template("show_meal.html", meal=meal, ingredients=ingredients))


def parse_ingred(dictionary):
	ing_list = []
	s = 'strIngredient1'
	for i in range(2,21):
		if dictionary[s]:
			ing_list.append(dictionary[s])
		if i >= 11:
			s= s[0:len(s)-2] + str(i)
		else:
			s= s[0:len(s)-1] + str(i)
	return ing_list
        
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
	

