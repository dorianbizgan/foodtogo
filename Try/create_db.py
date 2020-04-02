# beginning of create_db.py
import json
from models import app, db, Meal_Name, Meal_Category, Meal_Area, Meal_Ingredients, Meal_Instructions, Meal_Image


def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()
    return jsn

def create_meals():
    json_file = load_json('meals.json')
    meals = json_file['meals']
    for oneMeal in meals:
        idMeal = oneMeal['idMeal']
        meal_name = oneMeal['strMeal']
        category = oneMeal['strCategory']
        area = oneMeal['strArea']
        instructions = oneMeal['strInstructions']

        #ingred is the dictionary of all ingredients
        ingred = {}
        base1 = 'strIngredient'
        base2 = 'ingredient_'
        for i in range(1, 21):
            ingred[base2 + str(i)] = oneMeal[base1 + str(i)]

        #measure is the dictionary of all measures
        measure = {}
        base3 = 'strMeasure'
        base4 = 'measure_'
        for i in range(1, 21):
            measure[base4 + str(i)] = oneMeal[base3 + str(i)]

        image = oneMeal['strMealThumb']
                       

        newName = Meal_Name(meal_name = meal_name, idMeal = int(idMeal))
        newCategory = Meal_Category(idMeal = int(idMeal), category = category)
        newArea = Meal_Area(idMeal = int(idMeal), area = area)

        #adding only one ingredient and measure right now
        newIngredients = Meal_Ingredients(idMeal = int(idMeal),ingredient_1 = ingred['ingredient_1'], ingredient_2 = ingred['ingredient_2'], ingredient_3 = ingred['ingredient_3'],
                                          ingredient_4 = ingred['ingredient_4'], ingredient_5 = ingred['ingredient_5'], ingredient_6 = ingred['ingredient_6'],
                                          ingredient_7 = ingred['ingredient_7'],ingredient_8 = ingred['ingredient_8'],ingredient_9 = ingred['ingredient_9'],
                                          ingredient_10 = ingred['ingredient_10'],ingredient_11 = ingred['ingredient_11'],ingredient_12 = ingred['ingredient_12'],
                                          ingredient_13 = ingred['ingredient_13'],ingredient_14 = ingred['ingredient_14'],ingredient_15 = ingred['ingredient_15'],
                                          ingredient_16 = ingred['ingredient_16'],ingredient_17 = ingred['ingredient_17'],ingredient_18 = ingred['ingredient_18'],
                                          ingredient_19 = ingred['ingredient_19'],ingredient_20 = ingred['ingredient_20'],
                                          measure_1 = measure['measure_1'],measure_2 = measure['measure_2'],measure_3 = measure['measure_3'],measure_4 = measure['measure_4'],
                                          measure_5 = measure['measure_5'],measure_6 = measure['measure_6'],measure_7 = measure['measure_7'],measure_8 = measure['measure_8'],
                                          measure_9 = measure['measure_9'],measure_10 = measure['measure_10'],measure_11 = measure['measure_11'],measure_12 = measure['measure_12'],
                                          measure_13 = measure['measure_13'],measure_14 = measure['measure_14'],measure_15 = measure['measure_15'],measure_16 = measure['measure_16'],
                                          measure_17 = measure['measure_17'],measure_18 = measure['measure_18'],measure_19 = measure['measure_19'],measure_20 = measure['measure_20'])

        newInstructions = Meal_Instructions(idMeal = int(idMeal), instructions = instructions)

        #Need to make this work so that we can add all values for the ingredients and measures
        #for x,y in zip(ingred,measure):
            #newIngredients = Meal_Ingredients(idMeal = int(idMeal),  globals()[x] = ingred[x], globals()[y] = measure[y])
            #db.session.add(newIngredients)
        newImage = Meal_Image(idMeal = int(idMeal), image = image)
        
        # After I create the meal, I can then add it to my session. 
        db.session.add(newName)
        db.session.add(newCategory)
        db.session.add(newArea)
        db.session.add(newIngredients)
        db.session.add(newInstructions)
        db.session.add(newImage)

        
        # commit the session to my DB.
        db.session.commit()
	
create_meals()
# end of create_db.py
