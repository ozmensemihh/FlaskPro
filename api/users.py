from flask import Flask,Blueprint,jsonify

apiUsers =Blueprint('apiUser',__name__,url_prefix='/api/users')

@apiUsers.route("/")
def index():
    return jsonify({"success":True, "message":"User Page"})



@apiUsers.route("/<int:id>")
def user(id):
    return jsonify({"success":True, "userİd":id})
    
