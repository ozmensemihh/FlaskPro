from ecommerce.mdels import db
from ecommerce import createApp


def createDb():
    db.create_all(app=createApp())
