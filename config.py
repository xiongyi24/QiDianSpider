class Config():
    SECRET_KEY = 'hard to guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    JSON_AS_ASCII = False

    @staticmethod
    def init_app(app):
        pass


# TODO 隐私信息注意保护
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/test'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/test'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
