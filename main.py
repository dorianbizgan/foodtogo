from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import traceback
import requests
from cache_meals import meals, find_meal
from create_db import app, db, Meal_Name, Meal_Category, Meal_Area, Meal_Ingredients, Meal_Instructions, Meal_Image, create_meals
from sqlalchemy import func
from sqlalchemy import distinct

#adding break for HTML whenever there's a new line in instructions
#for meal in meals:
#   meal["strInstructions"] = meal["strInstructions"].replace('\n', '<br>')

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
    arg = request.args
    page = request.args.get('page', 1, type = int)
    meals = db.session.query(Meal_Name).paginate(page = page, per_page =10)
    return (render_template("meals.html", meals=meals))

@app.route('/meals/country/<string:country>')
def meals_country(country):
    
    page = request.args.get('page', 1, type = int)
    meals = db.session.query(Meal_Name).filter_by(area = country).paginate(page = page, per_page = 10)
    return (render_template("meal_country.html", meals=meals))


@app.route('/countries/')
def countries():
    countries = db.session.query(distinct(Meal_Area.area))
    return (render_template("countries.html", countries = countries))

@app.route('/meals/<int:meal_id>')
def show_meal(meal_id):

    #### REMOVE EVENTUALLY
    meal = find_meal(meal_id)
    ingredients = []
    amounts = []
    combined = []
    #### REMOVE EVENTUALLY

    meal_temp = db.session.query(Meal_Name.meal_name).filter(Meal_Name.idMeal == int(meal_id)).all() ### TESTING SQL QUERY
    meal = {"strMeal": str(meal_temp[0]).strip("[(u'").strip("','])")}
    #print(str(meal_temp[0]).strip("[(u'").strip("','])"))
    print(type(meal_temp[0]))

    for i in range(1,21):
        ingredient_num = "ingredient_" + str(i)
        measure_num = "measure_" + str(i)
        ingredient = db.session.query(getattr(Meal_Ingredients,ingredient_num)).filter(Meal_Ingredients.idMeal == int(meal_id)).all()
        measure = db.session.query(getattr(Meal_Ingredients,measure_num)).filter(Meal_Ingredients.idMeal == int(meal_id)).all()
        #for j in ingredient:
        ingredient = str(ingredient[0]).strip("(u'").strip("',)")
        measure    = str(measure[0]).strip("(u'").strip("',)")
        if ingredient == "None" or ingredient == "":
            continue
        combined.append({"ingredient":ingredient,"measure":measure})

        #print(str(ingredient)[0].strip("[(u'").strip("',)"))

    #   a = db.session.query(Meal_Ingredients.ingredient_num)
    #   b = db.session.query(Meal_)
    #for i in temp_ingredients:
    #   print(i)

    #temptemp = conn.execute(db.select("*").where(Meal_Ingredients.idMeal == int(meal_id)))
    #print(str(temptemp))
    '''
    for key in meal:
        if "strIngredient" in key and meal[key] != None and meal[key] != '':
            ingredients.append(meal[key])

        if "strMeasure" in key and meal[key] != None and meal[key] != '':
            amounts.append(meal[key])
            
    #print(str(ingredients) +  "\n" + str(amounts))
    for i in ingredients:
        try:
            combined.append({"ingredient":i,"measure":amounts[ingredients.index(i)]})
        except:
            continue
    '''
    ingredients = combined
    return(render_template("show_meal.html", meal=meal, ingredients=ingredients))
        
if __name__ == '__main__':
    app.run()
    

