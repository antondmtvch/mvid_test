import os
from pathlib import Path


class BaseConfig:
    DEBUG = False

    APP_HOST = '127.0.0.1'
    APP_PORT = 8080

    ROOT_DIR = Path(__file__).resolve().parent
    DATASET_PATH = os.path.join(ROOT_DIR, 'data/recommends.csv')


class DevelopmentConfig(BaseConfig):
    DEBUG = True
