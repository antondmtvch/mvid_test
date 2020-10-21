import os


class BaseConfig:
    DEBUG = False

    APP_HOST = '127.0.0.1'
    APP_PORT = 8080

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    DATASET_PATH = os.path.join(ROOT_DIR, 'data/recommends.csv')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
