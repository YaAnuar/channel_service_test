import os

class Config(object):
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/orders'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False
    # токен и id чата для telegram бота
    token = '1861574126:AAH2c9Mmt87CMB1FvRWUTxIOFvrpyEDo9dY'
    # установите ваш чат id, получить можно у бота @getmyid_bot
    chat_id = '828686133'

# return active config
available_configs = dict(development=DevelopmentConfig, production=ProductionConfig)
selected_config = os.getenv("FLASK_ENV", "production")
config = available_configs.get(selected_config, "production")