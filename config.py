import os

class Config:

    # SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY =os.environ.get('SECRET_KEY')

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://soleeh:soleeh..@localhost/minutepitch'



    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
