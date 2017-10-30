class Category:
    '''
    define the different category objects
    '''
    def __init__(self,date,content,title):
        self.date = date
        self.content = content
        self.title = title

class User(db.model):
    
