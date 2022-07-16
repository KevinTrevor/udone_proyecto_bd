from decouple import config

class Config:
    SECRET_KEY = config('SECRETKEY')

class DevelopmentConfig(Config):
    DEBUG = True
    UPLOAD_FOLDER = 'C:\images'
    

config = {
    'development' : DevelopmentConfig
}