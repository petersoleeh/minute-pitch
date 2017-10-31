from flask import render_template
from . import main


@main.route('/')
def index():
    '''
    landing page
    '''
    title = 'Minute pitch'

    return render_template('index.html',title =title)


@main.route('/categories/<id>')
def categories(id):
    '''
    new route that will display the contents of a specific category
    '''
    title = f'{id}'
    return render_template('categories.html',id = id)
