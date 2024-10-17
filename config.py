import os

class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dbProdutos.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False