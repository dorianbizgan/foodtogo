from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
app = Flask(__name__)

meals = [{"idMeal":"52768","strMeal":"Apple Frangipan Tart","strDrinkAlternate":None,"strCategory":"Dessert","strArea":"British","strInstructions":"Preheat the oven to 200C\/180C Fan\/Gas 6.\r\nPut the biscuits in a large re-sealable freezer bag and bash with a rolling pin into fine crumbs. Melt the butter in a small pan, then add the biscuit crumbs and stir until coated with butter. Tip into the tart tin and, using the back of a spoon, press over the base and sides of the tin to give an even layer. Chill in the fridge while you make the filling.\r\nCream together the butter and sugar until light and fluffy. You can do this in a food processor if you have one. Process for 2-3 minutes. Mix in the eggs, then add the ground almonds and almond extract and blend until well combined.\r\nPeel the apples, and cut thin slices of apple. Do this at the last minute to prevent the apple going brown. Arrange the slices over the biscuit base. Spread the frangipane filling evenly on top. Level the surface and sprinkle with the flaked almonds.\r\nBake for 20-25 minutes until golden-brown and set.\r\nRemove from the oven and leave to cool for 15 minutes. Remove the sides of the tin. An easy way to do this is to stand the tin on a can of beans and push down gently on the edges of the tin.\r\nTransfer the tart, with the tin base attached, to a serving plate. Serve warm with cream, cr\u00e8me fraiche or ice cream.","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/wxywrq1468235067.jpg","strTags":"Tart,Baking,Fruity","strYoutube":"https:\/\/www.youtube.com\/watch?v=rp8Slv4INLk","strIngredient1":"digestive biscuits","strIngredient2":"butter","strIngredient3":"Bramley apples","strIngredient4":"butter, softened","strIngredient5":"caster sugar","strIngredient6":"free-range eggs, beaten","strIngredient7":"ground almonds","strIngredient8":"almond extract","strIngredient9":"flaked almonds","strIngredient10":"","strIngredient11":"","strIngredient12":"","strIngredient13":"","strIngredient14":"","strIngredient15":"","strIngredient16":None,"strIngredient17":None,"strIngredient18":None,"strIngredient19":None,"strIngredient20":None,"strMeasure1":"175g\/6oz","strMeasure2":"75g\/3oz","strMeasure3":"200g\/7oz","strMeasure4":"75g\/3oz","strMeasure5":"75g\/3oz","strMeasure6":"2","strMeasure7":"75g\/3oz","strMeasure8":"1 tsp","strMeasure9":"50g\/1\u00beoz","strMeasure10":"","strMeasure11":"","strMeasure12":"","strMeasure13":"","strMeasure14":"","strMeasure15":"","strMeasure16":None,"strMeasure17":None,"strMeasure18":None,"strMeasure19":None,"strMeasure20":None,"strSource":None,"dateModified":None},{"idMeal":"52893","strMeal":"Apple & Blackberry Crumble","strDrinkAlternate":None,"strCategory":"Dessert","strArea":"British","strInstructions":"Heat oven to 190C\/170C fan\/gas 5. Tip the flour and sugar into a large bowl. Add the butter, then rub into the flour using your fingertips to make a light breadcrumb texture. Do not overwork it or the crumble will become heavy. Sprinkle the mixture evenly over a baking sheet and bake for 15 mins or until lightly coloured.\r\nMeanwhile, for the compote, peel, core and cut the apples into 2cm dice. Put the butter and sugar in a medium saucepan and melt together over a medium heat. Cook for 3 mins until the mixture turns to a light caramel. Stir in the apples and cook for 3 mins. Add the blackberries and cinnamon, and cook for 3 mins more. Cover, remove from the heat, then leave for 2-3 mins to continue cooking in the warmth of the pan.\r\nTo serve, spoon the warm fruit into an ovenproof gratin dish, top with the crumble mix, then reheat in the oven for 5-10 mins. Serve with vanilla ice cream.","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/xvsurr1511719182.jpg","strTags":"Pudding","strYoutube":"https:\/\/www.youtube.com\/watch?v=4vhcOwVBDO4","strIngredient1":"Plain Flour","strIngredient2":"Caster Sugar","strIngredient3":"Butter","strIngredient4":"Braeburn Apples","strIngredient5":"Butter","strIngredient6":"Demerara Sugar","strIngredient7":"Blackberrys","strIngredient8":"Cinnamon","strIngredient9":"Ice Cream","strIngredient10":"","strIngredient11":"","strIngredient12":"","strIngredient13":"","strIngredient14":"","strIngredient15":"","strIngredient16":"","strIngredient17":"","strIngredient18":"","strIngredient19":"","strIngredient20":"","strMeasure1":"120g","strMeasure2":"60g","strMeasure3":"60g","strMeasure4":"300g","strMeasure5":"30g","strMeasure6":"30g","strMeasure7":"120g","strMeasure8":"\u00bc teaspoon","strMeasure9":"to serve","strMeasure10":"","strMeasure11":"","strMeasure12":"","strMeasure13":"","strMeasure14":"","strMeasure15":"","strMeasure16":"","strMeasure17":"","strMeasure18":"","strMeasure19":"","strMeasure20":"","strSource":"https:\/\/www.bbcgoodfood.com\/recipes\/778642\/apple-and-blackberry-crumble","dateModified":None}]
for i in meals:
	for j in i:
		print(j, i[j])
	print()

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



@app.route('/state/new/', methods=['GET', 'POST'])
def newState():
    pass

        
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
	
