import os
import sys
import logging
import pandas as pd

from app.config import BaseConfig as conf

logging.basicConfig(level=logging.INFO)


def dataset2hd5():
    logging.info('Transform dataframe to hd5 format...')
    if os.path.exists(conf.HD5_PATH):
        logging.info(f'{conf.HD5_PATH} already exists')
        return
    try:
        data = pd.read_csv(conf.DATASET_PATH, names=conf.DATASET_COLS, dtype=conf.DATASET_DTYPES)
        data.to_feather(conf.HD5_PATH)
        logging.info(f'Completed! Save file to {conf.HD5_PATH}')
    except Exception as err:
        logging.error(err)
        sys.exit(1)


if __name__ == '__main__':
    dataset2hd5()
