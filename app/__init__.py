from flask import Flask
from app.models import db
from app.extensions import ma, cache, limiter
from app.blueprints.users.routes import users_bp
from app.blueprints.transactions.routes import transactions_bp
from app.blueprints.listings.routes import listings_bp
from app.blueprints.skills.routes import skills_bp
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_caching import Cache
import os


# Extension instances

ma = Marshmallow()
cache = Cache(config={'CACHE_TYPE': 'simple'})


def create_app(config_name="DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(f"config.{config_name}")


    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)
    

    # Enable CORS
    CORS(app, resources={r"/users/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

    # Register blueprints
    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(transactions_bp, url_prefix="/transactions")
    app.register_blueprint(listings_bp, url_prefix="/listings")
    app.register_blueprint(skills_bp, url_prefix="/skills")

    # with app.app_context():
    #     db.create_all()
    
    
    return app




# def create_app(config_name):
#     app = Flask(__name__)
#     app.config.from_object(f"config.{config_name}")

#     limiter = Limiter(key_func=get_remote_address, storage_uri=app.config['SQLALCHEMY_DATABASE_URI'])

#     # Initialize extensions
#     db.init_app(app)
#     ma.init_app(app)
#     limiter.init_app(app)
#     cache.init_app(app)

    

#     # Enable CORS
#     CORS(app, resources={r"/users/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

#     # Register blueprints
#     app.register_blueprint(users_bp, url_prefix="/users")
#     app.register_blueprint(transactions_bp, url_prefix="/transactions")
#     app.register_blueprint(listings_bp, url_prefix="/listings")
#     app.register_blueprint(skills_bp, url_prefix="/skills")

#     return app

# from flask import Flask
# import os

# def create_app(config=None):
#     app = Flask(__name__)

#     # Default config, can be overridden by custom config
#     if config:
#         app.config.from_mapping(config)
#     else:
#         # Load default or environment-specific config
#         app.config.from_object(os.getenv("FLASK_CONFIG", "config.Config"))

    

#     return app


# app = Flask(__name__)

    # # Load configuration
    # if config:
    #     app.config.from_mapping(vars(config))  
    # else:
    #     app.config.from_object(os.getenv("FLASK_CONFIG", "config.Config"))

    # # Ensure SQLALCHEMY_DATABASE_URI is present
    # if 'SQLALCHEMY_DATABASE_URI' not in app.config:
    #     raise RuntimeError("SQLALCHEMY_DATABASE_URI is not set in the app configuration.")

    # # Initialize extensions
    # db.init_app(app)
    # ma.init_app(app)
    # cache.init_app(app)