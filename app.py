# -- Flask Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

## Additional Imports
import datetime as dt
import model as model

# -- Initialization section --
app = Flask(__name__)
app.jinja_env.globals['current_time'] = dt.datetime.now()

# -- Routes --
@app.route('/')
@app.route('/index')
def index():
    data = {
    }
    return render_template('index.html', data=data)


@app.route('/games')
def games():
    data = {
    }
    return render_template('games.html', data=data)

@app.route('/add')
def add():
    data = {
    }
    return render_template('add.html', data=data)

@app.route('/about')
def about():
    data = {
    }
    return render_template('about.html', data=data)

@app.route('/acc')
def acc():
    data = {
    }
    return render_template('acc.html', data=data)



