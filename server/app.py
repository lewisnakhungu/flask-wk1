from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower 
from routes import register_routes

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)  

    register_routes(app)  # register routes after app/db are set

    return app

app = create_app()
