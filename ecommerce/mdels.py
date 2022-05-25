from dataclasses import dataclass
from unicodedata import category
from ecommerce import db


@dataclass
class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
  

    def __init__(self,id,username,email,password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
     


@dataclass
class Admin(db.Model):
    __tablename__= 'Admin'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    mod = db.Column(db.Integer)

    def __init__(self,id,username,email,password,mod):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.mod = mod

@dataclass
class Category(db.Model):
    __tablename__ = "Category"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))



@dataclass
class Product(db.Model):
    __tablename__="Product"


    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))
    price = db.Column(db.Float)
    oldPrice = db.Column(db.Float)
    description = db.Column(db.String(120))
    category_id = db.Column(db.Integer,db.ForeingKey("Category.id"))  