from . import db
class Category:
    '''
    define the different category objects
    '''
    def __init__(self,date,content,title):
        self.date = date
        self.content = content
        self.title = title

class User(db.model):
    __tablename__= 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
