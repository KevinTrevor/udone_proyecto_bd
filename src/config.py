from decouple import config

class Config:
    SECRETKEY = config('SECRETKEY')

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development' : DevelopmentConfig
}