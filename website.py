import json
from flask import Flask
from flask import render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
	return render_template('construction.html')

@app.route('/photography')
def photography():
	return render_template('photography.html')

@app.route('/teaching')
def teaching():
	return render_template('teaching.html')

@app.route('/traveling')
def traveling():
	return render_template('traveling.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

