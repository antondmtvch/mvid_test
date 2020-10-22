import pandas as pd


def get_recommendations(data: pd.DataFrame, sku: str, min_threshold: float) -> dict:
    if min_threshold:
        df = data.loc[((data.sku == sku) & (data.proba >= min_threshold)), ['recom', 'proba']]
    else:
        df = data.loc[data.sku == sku, ['recom', 'proba']]
    return df.to_dict(orient='records')
