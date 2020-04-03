#!flask/bin/python
import os
import unittest
from main import app, db
from create_db import create_meals, load_json
from models import *

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:HM 8767839393@localhost:5432/mealsdb')
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        create_meals()
        self.json_file = load_json("meals.json")

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_meals(self):
        # test data is loaded successfully
        db.drop_all()
        db.create_all()
        mealId1 = self.json_file["meals"][0]["idMeal"]
        # expect index out of bounds exception
        with self.assertRaises(IndexError):
            response = self.app.get("/meals/"+str(mealId1))
        create_meals()
        all_meals = Meal_Name.query.all()
        self.assertEqual(len(all_meals), len(self.json_file["meals"]))
        response = self.app.get("/meals/"+str(mealId1))
        self.assertEqual(response.status, "200 OK")


    def test_meal_category_exist(self):
        # test meal category is present in category page
        response = self.app.get("/categories", follow_redirects=True)
        self.assertEqual(response.status, "200 OK")
        meals = self.json_file['meals']
        count = 0
        for oneMeal in meals:
            idMeal1 = oneMeal['idMeal']
            meal_category = Meal_Category.query.filter(Meal_Category.idMeal == idMeal1).first()
            self.assertTrue(meal_category.category in str(response.data))
            count += 1
        # check if all meals have been tested
        all_meals = Meal_Name.query.all()
        self.assertEqual(count, len(all_meals))


    def test_meal_area_exist(self):
        # test meal country/area exists in countries page
        response = self.app.get("/countries", follow_redirects=True)
        self.assertEqual(response.status, "200 OK")
        meals = self.json_file['meals']
        count = 0
        for oneMeal in meals:
            idMeal1 = oneMeal['idMeal']
            meal_area = Meal_Area.query.filter(Meal_Area.idMeal == idMeal1).first()
            self.assertTrue(meal_area.area in str(response.data))
            count += 1
        # check if all meals have been tested
        all_meals = Meal_Name.query.all()
        self.assertEqual(count, len(all_meals))


if __name__ == '__main__':
    unittest.main()
