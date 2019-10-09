from flask import Flask, render_template, request
from flask_flatpages import FlatPages
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'


app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>/')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html', page=page)

@app.route('/projects')
def projects():
	return render_template('projects.html')

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