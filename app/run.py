import os
import numpy as np
import pandas as pd

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)


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


def get_recommendations(sku: str, min_threshold: float) -> dict:
    data = app.config['DATA']
    if min_threshold:
        df = data.loc[((data.sku == sku) & (data.proba >= min_threshold)), ['recom', 'proba']]
    else:
        df = data.loc[data.sku == sku, ['recom', 'proba']]
    return df.to_dict(orient='records')


@app.route('/')
def index():
    return 'hello'


@app.route('/recommendations', methods=['GET'])
def recommendations_handler():
    sku = request.args.get('sku', type=str)
    threshold = request.args.get('min_threshold', type=float)
    if sku:
        try:
            recommendations = get_recommendations(sku, threshold)
            return jsonify(sku=sku, recommendations=recommendations)
        except Exception as err:
            app.logger.error(err)
            return make_response(jsonify(error='Unexpected error', status=500), 500)
    return make_response(jsonify(error='Parameter "sku" is required ', status=400), 400)


def run_app(app_inst):
    app_inst.config.from_object('config.DevelopmentConfig')
    app_inst.config.from_mapping(
        DATA=load_dataset(app_inst.config['DATASET_PATH'])
    )
    app.run(app.config['APP_HOST'], app.config['APP_PORT'], threaded=True)


if __name__ == '__main__':
    run_app(app)
