from flask import Flask
from models import db, migrate  # Now safe to import
from models import Hero, Power, HeroPower  # models need to be loaded
from routes import register_routes  # import routes after app is created

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    register_routes(app)

    return app

app = create_app()
