import os

class Config:
    SECRET_KEY = "your_secret_key"
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:Migmaster10!@localhost/skillx_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False








































# os.environ.get('SQLALCHEMY_DATABASE_URI')
# class DevelopmentConfig:
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# class ProductionConfig:
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False


# # config.py

# class Config:
#     SECRET_KEY = "your_secret_key"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:password@localhost/your_db"



# class TextingConfig:
#     pass

# class ProductionConfig:
#     pass
# config.py