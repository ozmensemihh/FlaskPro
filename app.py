
from flask import Flask,jsonify
from api.users import apiUsers
from api.products import apiProducts
from api.admin import apiAdmin
from api.categories import apiCategory
from ecommerce import createApp
from ecommerce.initialize import createDb


app =createApp()
createDb()

app.register_blueprint(apiUsers)
app.register_blueprint(apiProducts)
app.register_blueprint(apiAdmin)
app.register_blueprint(apiCategory)


@app.route("/")
def index():
    return jsonify({"success":True,"message":"Main Page"})


if __name__ == "__main__":
    app.run(debug = True)