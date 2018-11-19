import os


class Config:
    SECRET_KEY = 'e23e8f9e119d62e3dc30b88fce520c54c'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///web.database'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
