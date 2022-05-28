from dataclasses import dataclass
from itertools import product
from select import select
from unicodedata import category
from ecommerce import db
from werkzeug.security import generate_password_hash


@dataclass
class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    activated = db.Column(db.Boolean,default=True)
  

    def __init__(self,id,username,email,password,activated):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.activated = activated


    @classmethod
    def get_all_users(cls):
        return cls.query.all()    

    @classmethod
    def get_user_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_user(cls,username,email,password):
        user = cls(None,username,email,password,True)
        db.session.add(user)
        db.session.commit()       

    @classmethod
    def update_user(cls,id,username,email,password,activated):
        user=cls.get_user_by_id(id)
        user.username=username
        user.email = email
        user.password = password
        user.activated = activated
        db.session.commit()   

    @classmethod
    def delete_user(cls,id):
        user = cls.get_user_by_id(id).first()
        db.session.delete(user)
        db.session.commmit()

    @classmethod
    def activate_user (cls,id):
        user = cls.query.filter_by(id=id).first()
        user.activated = True
        db.session.commit()    

    @classmethod
    def deactivate_user (cls,id):
        user = cls.query.filter_by(id=id).first()
        user.activated = False
        db.session.commit()             


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

    @classmethod
    def get_all_admins(cls):
        return cls.query.all()

    @classmethod
    def get_admin_by_id(cls,id):
        return cls.query.filter_by(id=id).first()    

    @classmethod
    def add_admin(cls,username,email,password):
        admin= cls(None,username,email,generate_password_hash(password),0)
        db.session.add(admin)
        db.session.commit()    

    @classmethod
    def update_admin(cls,id,username,email,password,mod):
        admin = cls.get_admin_by_id(id).first()
        admin.username = username
        admin.email = email
        admin.password = generate_password_hash(password)
        admin.mod = mod
        db.session.commit()    

    @classmethod
    def delete_admin(cls,id):
        admin = cls.get_admin_by_id(id).first()
        db.session.delete(admin)
        db.session.commit()    


@dataclass
class Category(db.Model):
    __tablename__ = "Category"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))

    @classmethod
    def get_all_categories(cls):
        return cls.query.all()

    @classmethod
    def get_category_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def add_category(cls,name):
        category = cls(name)
        db.session.add(category)
        db.session.commit()  

    @classmethod
    def update_category(cls,id,name):
        category = cls.get_category_by_id(id).first()
        category.name = name
        db.session.commit()      

    @classmethod
    def delete_category(cls,id):
        category=cls.get_category_by_id(id).first()
        db.session.delete(category)
        db.session.commit()    


@dataclass
class Product(db.Model):
    __tablename__="Product"


    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(120))
    price = db.Column(db.Float)
    oldPrice = db.Column(db.Float)
    description = db.Column(db.String(120))
    category_id = db.Column(db.Integer,db.ForeignKey('Category.id'))


    def __init__(self,id,name,price,oldprice,description,category_id):
        self.name = name
        self.price = price
        self.id = id
        self.oldPrice = oldprice
        self.description = description
        self.category_id = category_id


    @classmethod
    def get_all_products(cls):
        return cls.query.all()

    @classmethod
    def get_product_by_id(cls,id):
        return cls.query.filter_by(id=id).first()    

    @classmethod
    def add_product(cls,name,price,oldprice,description,category_id):
        product=cls(name,price,oldprice,description,category_id)
        db.session.add(product)
        db.session.commit()    


    @classmethod
    def update_product(cls,id,name,price,oldprice,descripton,category_id):
        product = cls.get_product_by_id(id).first()
        product.name = name
        product.price = price
        product.oldprice  =oldprice
        product.description  = descripton
        product.category_id = category_id
        db.session.commmit()

    @classmethod
    def delete_product(cls,id):
        product = cls.get_product_by_id(id).first()
        db.session.delete(product)
        db.session.commit()    
