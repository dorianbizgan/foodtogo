#parsing 
import requests

def parse_meals():
	meals= []
	alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	url = "https://www.themealdb.com/api/json/v1/1/search.php?f=a"
	for i in range(1,26):
		r = requests.get(url)
		d = r.json()
		meal_list = []
		d1 = {}
		for key in d:
			meal_list = d[key]
		try:
			for dicts in meal_list:
				meals.append(dicts)
		except:
			pass
		url = url[0:len(url)-1] + alph[i]
	print(meals)
	return meals
parse_meals()