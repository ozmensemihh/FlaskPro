from flask import Flask,Blueprint,jsonify

from ecommerce.mdels import Admin

apiAdmin =Blueprint('apiAdmin',__name__,url_prefix='/api/admins')

@apiAdmin.route("/")
def index():
    return jsonify({"success":True, "message":"Admin Page"})

@apiAdmin.route("/admins")
def admins():
    adminslist = []
    admins = Admin.get_all_admins()

    for admin in admins:
        adminslist.append({"id":admin.id,"name":admin.username,"email":admin.email,"password":admin.password,"mod":admin.mod})

    return jsonify({"success":True, "data":adminslist,"count":len(adminslist)})