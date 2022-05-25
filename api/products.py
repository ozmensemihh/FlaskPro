from flask import Flask,Blueprint,jsonify

apiProducts =Blueprint('apiProduct',__name__,url_prefix='/api/products')

@apiProducts.route("/")
def index():
    return jsonify({"success":True, "message":"Product Page"})
