from flask import render_template
from app import app


@app.route('/')
def index():
    '''
    landing page
    '''
    title = 'Minute pitch'

    return render_template('index.html',title =title)


@app.route('/categories/<id>')
def categories(id):
    '''
    new route that will display the contents of a specific category
    '''
    title = f'{id}'
    return render_template('categories.html',id = id)
