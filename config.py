
class Config(object):
    DEBUG = True
    TESTING = False
    AIRTABLE_KEY = 'keyaaaaa11111'

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
