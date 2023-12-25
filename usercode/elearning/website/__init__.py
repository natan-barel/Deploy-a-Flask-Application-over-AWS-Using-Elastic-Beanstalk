from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import json

# Databse object and name
db = SQLAlchemy()
DB_NAME = "courses_database.db"

def create_app():
    # Creating new App
    app = Flask(__name__)
    # Adding a simple secret key
    app.config['SECRET_KEY'] = 'this is a simple secret key'
    
    # Adding Database to the application
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Adding URL's
    from .auth import auth
    app.register_blueprint(auth, url_prefix='/')
    create_datebase(app)
    return app


def create_datebase(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print("Database Created")
