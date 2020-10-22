import os
import numpy as np
from pathlib import Path


class BaseConfig:
    DEBUG = False

    APP_HOST = '127.0.0.1'
    APP_PORT = 5000

    ROOT_DIR = Path(__file__).resolve().parent.parent
    DATASET_PATH = os.path.join(ROOT_DIR, 'data/recommends.csv')
    HD5_PATH = os.path.join(ROOT_DIR, 'data/recommends.hd5')

    DATASET_COLS = ('sku', 'recom', 'proba')
    DATASET_DTYPES = {
        'sku': 'category',
        'recom': 'category',
        'proba': np.float16
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = True
