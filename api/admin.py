from werkzeug.security import generate_password_hash
from flask import Flask,Blueprint,jsonify,request


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

@apiAdmin.route("/addAdmin", methods = ["GET","POST"])
def addAdmin():
    try:
        if request.method == 'POST':
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")
            
            if username == None and email == None and password == None:
                return jsonify({"success":False, "message":"Missing fields"})
      
            Admin.add_admin(username,email,password)

        return jsonify({"success":True, "message":"User Added"})    
    except Exception as e:
       return jsonify({"success":False, "message":"User Added hata"})     