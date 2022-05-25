from flask import Flask,Blueprint,jsonify

apiCategory =Blueprint('apiCategory',__name__,url_prefix='/api/categories')

@apiCategory.route("/")
def index():
    return jsonify({"success":True, "message":"Category Page"})
