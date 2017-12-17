class BaseConfig(object):
    
    SECRET_KEY = 'makesure to set a very secret key'
    INDEX_PRE_PAGE = 9
    ADMIN_PRE_PAGE = 15


class DevelopmentConfig(BaseConfig):
    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:zmxhdu@localhost:3306/recruiment?charset=utf8'


class ProductionConfig(BaseConfig):
    
    pass


class TestingConfig(BaseConfig):
    
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
