from flask import Flask,Blueprint,jsonify

apiAdmin =Blueprint('apiAdmin',__name__,url_prefix='/api/admins')

@apiAdmin.route("/")
def index():
    return jsonify({"success":True, "message":"Admin Page"})
