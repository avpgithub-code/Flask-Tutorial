from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db_alchemy = SQLAlchemy()

def create_app():
    app = Flask(__name__,template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
    
    db_alchemy.init_app(app)
    from routes import register_routes
    
    
    migrate = Migrate(app,db_alchemy)
    return app
