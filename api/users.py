
import email
from flask import Flask,Blueprint,jsonify, request
from ecommerce.mdels import User
from werkzeug.security import generate_password_hash,check_password_hash

apiUsers =Blueprint('apiUser',__name__,url_prefix='/api/users')

@apiUsers.route("/")
def index():
    return jsonify({"success":True, "message":"User Page"})

@apiUsers.route("/users")
def users():
    userlist = []
    users = User.get_all_users()

    for user in users:
        userlist.append({"id":user.id,"name":user.username,"email":user.email,"password":user.password})

    return jsonify({"success":True, "data":userlist,"count":len(userlist)})


@apiUsers.route("/<int:id>",methods = ["GET","DELETE","PUT"])
def user(id):
    try:
        user = User.get_user_by_id(id)
        
        if user :
            return jsonify({"success":False,"message":"User not found "})  

        if request.form == "GET":
            userobj = {"id":user.id,"name":user.name,"email":user.email,"password":user.password,"activated":user.activated}
            return jsonify({"success":True, "user":userobj})
    
        elif request.form == "DELETE": 
            User.delete_user(id)   
            return jsonify({"success":True,"message":"User deleted"})  

        elif request.form == "PUT":
            username= request.form.get("username")
            email =  request.form.get("email")
            password= request.form.get("password")

            if user.username == None:
                username = user.username
            if user.username == None:
                email = user.email
            if user.password == None:
                password = user.password 
            
            User.update_user(id,username,email,generate_password_hash(password))     
            return jsonify({"success":True, "message":"User updated"})

    except Exception as e:
        return jsonify({"success":False,"message":"hata olustu"})

@apiUsers.route("/addUser",methods=['GET','POST'])
def addUser():
    try:
        if request.method == 'POST':
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")

            if username == None and email == None and password == None:
                return jsonify({"success":False, "message":"Missing fields"})

            hashed_password = generate_password_hash(password)        

            User.add_user(username,email,hashed_password)


        return jsonify({"success":True, "message":"User Added"})    
    except Exception as e:
       return jsonify({"success":False, "message":"User Added hata"})     


@apiUsers.route("/activateUser",methods = ["POST"])
def activateUser():
    try:
        if request.form:
            id = request.form.get(id)
            user = User.get_user_by_id(id)
            if user is None:
                return jsonify({"success":False,"message":"User not found"})

            if user.activated == True:
                return jsonify({"success":False,"message":"User already activated"})

            User.activate_user(id)    

            return jsonify({"success":True,"message":"User activated"})

    except Exception as e:
         return jsonify({"success":False,"message":"Hata oluştu"})      

@apiUsers.route("/deactivateUser",methods= ["POST"])
def deactivateUser():
    try:
        if request.form:
            id = request.form.get(id)
            user = User.get_user_by_id(id)

            if user is None:
                return jsonify({"success":False,"message":"User not found"}) 

            if user.activate == False:
                return jsonify({"success":False,"message":"User already deactivate"}) 

            User.deactivate_user(id)
            return jsonify({"success":True,"message":"User deactivated"}) 
    except Exception as a:
        return jsonify({"success":False,"message":"Hata olustu"})             



@apiUsers.route("/activateUsers")
def deactivateUsers():
    try:
        userlist = []
        users = User.get_all_users()

        for user in users:
            if user.activate == False:
                userlist.appent({"id":user.id,"name":user.username,"email":user.email,"password":user.password,"activated":user.actvated})
        return jsonify({"success":True, "data":userlist,"count":len(userlist)})
    except Exception as e:
       return jsonify({"success":False, "message":"hata olustu"})     

@apiUsers.route("activateUsers")
def activateUsers():
    try:
        userlist = []
        users = User.get_all_users()

        for user in users:
            if user.activate == True:
                userlist.appent({"id":user.id,"name":user.username,"email":user.email,"password":user.password,"activated":user.actvated})

        return jsonify({"success":True, "data":userlist,"count":len(userlist)})
    except Exception as e:
       return jsonify({"success":False, "message":"hata olustu"})           