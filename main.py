from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
import traceback
from create_db import app, db, Meal_Name, Meal_Category, Meal_Area, Meal_Ingredients, Meal_Instructions, Meal_Image, create_meals
from sqlalchemy import func
from sqlalchemy import distinct
import sys
import subprocess
#import re
#from sqlalchemy import join
#from sqlalchemy.sql import select
#if sys.version_info.major < 3:
#    reload(sys)
#sys.setdefaultencoding('utf8')



@app.route('/', methods=['GET','POST'])
def home():
    arg = request.args
    page = request.args.get('page', 1, type = int)
    if(request.method == 'POST'):
        name = request.form['name']
        if(len(name)!=0):
            meals = db.session.query(Meal_Name).filter(Meal_Name.meal_name.ilike("%" + str(name) + "%")).paginate(page = page, per_page =10)
            return(render_template('meals.html', meals=meals))
    else:
        return render_template("index.html")

@app.route('/about-us/', methods = ['GET','POST'])
def aboutUs():
    blank = ""


    if request.method == 'POST':
        p = subprocess.Popen(["coverage", "run", "--branch", "tests.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                stdin=subprocess.PIPE)
        out, err = p.communicate()
        output=err+out
        output = output.decode("utf-8") #convert from byte type to string type
        output = str(output) #convert from byte type to string type
        # create_meals()
        return (render_template("aboutUs.html", output = "<br/>".join(output.split("\n"))))




    else:
        return render_template("aboutUs.html", output = blank)

@app.route('/categories/', methods=['GET', 'POST'])
def categories():
    arg = request.args
    page = request.args.get('page', 1, type = int)
    if(request.method == 'POST'):
        name = request.form['name']
        if(len(name)!=0):
            categories = db.session.query(distinct(Meal_Category.category)).filter(Meal_Category.category.ilike("%" + str(name) + "%")).paginate(page = page, per_page =10)
            return(render_template('categories.html', categories=categories))
    else:
        categories  = db.session.query(distinct(Meal_Category.category)).paginate(page = page, per_page =10)
        return (render_template("categories.html", categories = categories))


@app.route('/meals/',methods = ['GET','POST'])
def meals():
    
    arg = request.args
    page = request.args.get('page', 1, type = int)
    search = request.args.get('search')
    #print(search, type(search))
    #print(page, type(page))
    try:
        name = request.form['name']
        search = name
        page = 1
    except:
        pass
    
    if(request.method == 'POST'):
        name = request.form['name']
        search=name
        #print(name)
        if(len(name)!=0):
            #Object.column.op('regexp')(REGEX)
            meals = db.session.query(Meal_Name).filter(Meal_Name.meal_name.ilike("%" + name + "%")).paginate(page = page, per_page=10)
            #meals = db.session.query(Meal_Name).filter(Meal_Name.meal_name.ilike("%" + name + "%")).paginate(page = page, per_page =10)
            return(render_template('meals.html', meals=meals, search=search))
        
    elif search != None:
        meals = db.session.query(Meal_Name).filter(Meal_Name.meal_name.ilike("%" + search + "%")).paginate(page = page, per_page=10)
        return (render_template("meals.html", meals=meals, search=search))
    else:
        meals = db.session.query(Meal_Name).paginate(page = page, per_page =10)#all()
        #print(db.session.query(Meal_Name))
        return (render_template("meals.html", meals=meals, search=search))

@app.route('/cuisines/', methods = ['GET','POST'])
def cuisines():
    arg = request.args
    page = request.args.get('page', 1, type = int)
    if(request.method == 'POST'):
        page = 1
        name = request.form['name']
        if(len(name)!=0):
            cuisines = db.session.query(distinct(Meal_Area.area)).filter(Meal_Area.area.ilike("%" + str(name) + "%")).paginate(page = page, per_page =10)
            return(render_template('cuisines.html', cuisines=cuisines))
    else:
        cuisines = db.session.query(distinct(Meal_Area.area)).paginate(page = page, per_page =10)
        return(render_template("cuisines.html", cuisines = cuisines))

@app.route('/cuisines/<cuisine>',methods = ['GET','POST'])
def get_cuisine(cuisine):
    arg = request.args
    page = request.args.get('page', 1, type = int)
    if(request.method == 'POST'):
        page = 1
        name = request.form['name']
        if(len(name)!=0):
            meals = db.session.query(Meal_Name).join(Meal_Area, Meal_Name.idMeal == Meal_Area.idMeal).filter(Meal_Name.meal_name.ilike("%" + str(name) + "%")).filter(Meal_Area.area==cuisine).paginate(page = page, per_page =10)
            return(render_template('meals.html', meals=meals))
    else:
        meals = db.session.query(Meal_Name).join(Meal_Area, Meal_Name.idMeal == Meal_Area.idMeal).filter(Meal_Area.area==cuisine).paginate(page = page, per_page =10)
        return(render_template('meal_cuisine.html', meals=meals, cuisine = cuisine))

@app.route('/categories/<category>',methods = ['GET','POST'])
def get_category(category):
    arg = request.args
    page = request.args.get('page', 1, type = int)
    if(request.method == 'POST'):
        name = request.form['name']
        if(len(name)!=0):
            meals = db.session.query(Meal_Name).join(Meal_Category, Meal_Name.idMeal == Meal_Category.idMeal).filter(Meal_Name.meal_name.ilike("%" + str(name) + "%")).filter(Meal_Category.category==category).paginate(page = page, per_page =10)
            return(render_template('meals.html', meals=meals))
    else:
        meals = db.session.query(Meal_Name).join(Meal_Category, Meal_Name.idMeal == Meal_Category.idMeal).filter(Meal_Category.category==category).paginate(page = page, per_page =10)
        return(render_template('meal_category.html', meals=meals, category = category))
    
@app.route('/meals/<int:meal_id>', methods = ['GET','POST'])
def show_meal(meal_id):
        arg = request.args
        page = request.args.get('page', 1, type = int)
        if(request.method == 'POST'):
            name = request.form['name']
            print(name)
            if(len(name)!=0):
                #Object.column.op('regexp')(REGEX)
                meals = db.session.query(Meal_Name).filter(Meal_Name.meal_name.ilike("%" + str(name) + "%")).paginate(page = page, per_page =10)
                return(render_template('meals.html', meals=meals))

        
        #name_ins = db.session.query(Meal_Name, Meal_Instructions).join(Meal_Instructions, Meal_Name.idMeal == Meal_Instructions.idMeal).filter(Meal_Name.idMeal == int(meal_id)).all()
        name =  db.session.query(Meal_Name).filter(Meal_Name.idMeal == int(meal_id)).all()
        ins = db.session.query(Meal_Instructions).filter(Meal_Instructions.idMeal == int(meal_id)).all()
        #ins = re.split("[.\r\n]", ins[0].instructions)
        ins =  ins[0].instructions.split('.\r\n')
        ingredients = db.session.query(Meal_Ingredients).filter(Meal_Ingredients.idMeal==int(meal_id)).all()
        image = db.session.query(Meal_Image).filter(Meal_Image.idMeal==int(meal_id)).all()
        ing = []
        mes = []
        for i in range(1,21):
            ingredient_num = "ingredient_" + str(i)
            measure_num = "measure_" + str(i)
            val1 = getattr(ingredients[0], ingredient_num)
            val2 = getattr(ingredients[0], measure_num)
            if(val1 != '' and val1 is not None):
                ing.append(val1)
                mes.append(val2)
        return(render_template("show_meal.html", name = name, ins = ins, image = image, ingredients = ing, measure = mes))

if __name__ == '__main__':
    app.debug = True
    app.run()
	

