from flask import Flask
from .main.routes import main
from .extensions import mongo


def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = ''
    app.register_blueprint(main)
    mongo.init_app(app)

    return app
