from flask import Flask,Blueprint,jsonify, request
from ecommerce.mdels import User

apiUsers =Blueprint('apiUser',__name__,url_prefix='/api/users')

@apiUsers.route("/")
def index():
    return jsonify({"success":True, "message":"User Page"})



@apiUsers.route("/<int:id>")
def user(id):
    return jsonify({"success":True, "userİd":id})
    

@apiUsers.route("/addUser",methods=['GET','POST'])
def addUser():
    if request.method == 'POST':
        user  = User (None,
        request.form.get("username"),
        request.form.get("email"),
        request.form.get("password"))
        user.addUser()
    return jsonify({"success":True, "message":"User Added"})    
