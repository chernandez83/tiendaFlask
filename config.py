class Config:
    SECRET_KEY = 'u5+y]:AL26Pw!mm$,WGQ"}]^_7x5Pe&,wPumYGw!mm$:2(p#D'

class DevelopmentConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}