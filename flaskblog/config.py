import os
from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')#'1104570453007afbe0960d9f562a001f'
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')#'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')