from flask import Flask, render_template, request, redirect, url_for, jsonify
import random
app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")
@app.route('/about-us/')
def aboutUs():
    pass

@app.route('/state/new/', methods=['GET', 'POST'])
def newState():
    pass

        
if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
	

