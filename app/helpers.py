import os
import pandas as pd
import numpy as np


def load_dataset(path: str) -> pd.DataFrame:
    colnames = ('sku', 'recom', 'proba')
    dtypes = {
        'sku': 'category',
        'recom': 'category',
        'proba': np.float16
    }
    hdf_path = os.path.splitext(path)[0] + '.h5'
    try:
        data = pd.read_feather(hdf_path, columns=colnames)
    except FileNotFoundError:
        data = pd.read_csv(path, names=colnames, dtype=dtypes)
        data.to_feather(hdf_path)
    return data


def get_recommendations(data: pd.DataFrame, sku: str, min_threshold: float) -> dict:
    if min_threshold:
        df = data.loc[((data.sku == sku) & (data.proba >= min_threshold)), ['recom', 'proba']]
    else:
        df = data.loc[data.sku == sku, ['recom', 'proba']]
    return df.to_dict(orient='records')
