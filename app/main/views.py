from flask import render_template,url_for,abort
from . import main
from ..models import Category,Comment,User,Pitch
# from ..models import get_category
from flask_login import login_required
from .forms import CommentForm
from .. import db


@main.route('/')
def index():
    '''
    landing page
    '''
    title = 'Minute pitch'
    category = Category.get_category()

    return render_template('index.html', title = title,category=category)


@main.route('/categories/<int:id>')
def categories(id):
    '''
    new route that will display the contents of a specific category
    '''
    title = f'{id}'
    return render_template('categories.html',id = id)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


# comment section
# @main.route('/categories/comment/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_comment(id):
#
#     form = CommentForm()
#
#     if form.validate_on_submit():
#         title = form.title.data
#         comment = form.comment.data
#
#
#         new_comment.save_comment()
#         return redirect(url_for('login')
#
#
#     return render_template('new_comment.html')
