#!flask/bin/python
import os
import unittest
from main import app, db
from create_db import create_meals, load_json
from models import *
from flask import request

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:lionking@localhost:5432/mealsdb')
        self.app = app.test_client()
        db.session.remove()

        db.drop_all()
        db.create_all()
        create_meals()
        self.json_file = load_json("meals.json")

    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()

    def test_create_meals(self):
        # test data is loaded successfully
        db.drop_all()
        db.create_all()
        mealId1 = self.json_file["meals"][0]["idMeal"]
        # expect index out of bounds exception
        with self.assertRaises(IndexError):
            response = self.app.get("/meals/"+str(mealId1))
        create_meals()
        all_meals = db.session.query(Meal_Name).all()
        self.assertEqual(len(all_meals), len(self.json_file["meals"]))
        response = self.app.get("/meals/"+str(mealId1))
        self.assertEqual(response.status, "200 OK")


    def test_meal_category_exist(self):
        # test meal category is present in category page
        responses = []
        for i in range(1,3):
            response = self.app.get("/categories/?page=" + str(i), follow_redirects=True)
            responses.append(response)
            #print(response)
            self.assertEqual(response.status, "200 OK")
        self.assertEqual(len(responses),2)
        meals = self.json_file['meals']
        #print(meals)
        count = 0
        for response in responses:
            for oneMeal in meals:
                idMeal1 = oneMeal['idMeal']
                meal_category = db.session.query(Meal_Category).filter(Meal_Category.idMeal == idMeal1).first()
                #print(meal_category.category)
                #print(response.data)
                if meal_category.category in str(response.data):
                    count += 1
        # check if all meals have been tested
        all_meals = db.session.query(Meal_Name).all()
        self.assertEqual(count, len(all_meals))


    def test_meal_area_exist(self):
        # test meal country/area exists in countries page
        responses = []
        for i in range(1,4):
            response = self.app.get("/cuisines/?page=" + str(i), follow_redirects=True)
            responses.append(response)
            self.assertEqual(response.status, "200 OK")
        self.assertEqual(len(responses), 3)
        meals = self.json_file['meals']
        count = 0
        areas = set()
        for response in responses:
            for oneMeal in meals:
                idMeal1 = oneMeal['idMeal']
                meal_area = Meal_Area.query.filter(Meal_Area.idMeal == idMeal1).first()
                if meal_area.area in str(response.data):
                    count += 1
                    areas.add(oneMeal['idMeal'])

        # check if all meals have been tested
        all_meals = Meal_Name.query.all()
        self.assertEqual(len(areas), len(all_meals))

        # try:
        #     db.create_all()
        #     create_meals()
        # except:
        #     pass
if __name__ == '__main__':
    unittest.main()
