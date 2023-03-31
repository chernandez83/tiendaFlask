from decouple import config

class Config:
    SECRET_KEY = 'u5+y]:AL26Pw!mm$,WGQ"}]^_7x5Pe&,wPumYGw!mm$:2(p#D'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    #MYSQL_PASSWORD='123456'
    MYSQL_DB='tiendaflask'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'cut.netjliz@gmail.com'
    MAIL_PASSWORD = config('MAIL_PASSWORD')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}