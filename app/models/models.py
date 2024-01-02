from database import db
class Base(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
class Books(Base):
    name = db.Column(db.String(100), nullable = False)
    author = db.Column(db.String(100), nullable = False)
    publisher = db.Column(db.String(100), nullable = False)
    def __init__(self,name,author,publisher):
        self.name = name
        self.author = author
        self.publisher = publisher
    def serialize(self):
        return {
            "name" : self.name,
            "author": self.author,
            "publisher" : self.publisher
        }
class Movie(Base):
    name = db.Column(db.String(100), nullable = False)
    actor = db.Column(db.String(100), nullable = False)
    director = db.Column(db.String(100), nullable = False)
    def __init__(self,name,actor,director):
        self.name = name
        self.actor = actor
        self.director = director
    def serialize(self):
        return {
            "name" : self.name,
            "actor": self.actor,
            "director" : self.director
        }
    
class User(Base):
    name = db.Column(db.String(100), nullable = False)
    Uname = db.Column(db.String(100), nullable = False,unique=True)
    Upass= db.Column(db.String(100), nullable = False)
    def __init__(self,name,Uname,Upass):
        self.name = name
        self.Uname = Uname
        self.Upass = Upass
    def serialize(self):
        return {
            "name" : self.name,
            "Uname": self.Uname,
            "Upass" : self.Upass
        }