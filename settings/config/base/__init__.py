from umba_lib.helpers.env import env


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = env.str("SECRET_KEY", default="123456asdfghjkl;.,mnbvcxz")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 280
    SQLALCHEMY_POOL_TIMEOUT = 20
    PER_PAGE = 1
