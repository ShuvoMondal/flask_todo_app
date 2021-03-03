from flask import Flask
from .main.routes import main
from .extensions import mongo

def create_app():
    app=Flask(__name__)
    app.config['MONGO_URI'] = 'mongodb+srv://admin:admin123@cluster0.x9lhp.mongodb.net/mydb?retryWrites=true&w=majority'
    app.register_blueprint(main)
    mongo.init_app(app)

    return app