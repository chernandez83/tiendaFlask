from decouple import config

class Config:
    SECRET_KEY = 'u5+y]:AL26Pw!mm$,WGQ"}]^_7x5Pe&,wPumYGw!mm$:2(p#D'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    #MYSQL_PASSWORD='123456'
    MYSQL_DB='tiendaflask'
    MAIL_SERVER = 'smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config('MAIL_USERNAME')
    MAIL_PASSWORD = config('MAIL_PASSWORD')
    MAIL_SENDER = config('MAIL_SENDER')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}