#parsing
import json
import requests
meals= []
alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","v","w","y"]
url = "https://www.themealdb.com/api/json/v1/1/search.php?f="

url_a = url+alph[0]
r = requests.get(url_a)
store = r.json()
for i in range(1,len(alph)):
    new_url = url+alph[i]
    r = requests.get(new_url)
    d = r.json()
    d = d['meals']
    print(alph[i])
    for ele in d:
        store['meals'].append(ele)


with open('meals.json', 'w') as fp:
        json.dump(store, fp, indent=4)
