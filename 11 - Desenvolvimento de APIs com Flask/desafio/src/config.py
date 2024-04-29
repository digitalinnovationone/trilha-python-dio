import os


class Config:
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///bank.sqlite"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite://"
