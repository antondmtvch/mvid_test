from flask import jsonify, request, make_response

from app import app
from app.helpers import get_recommendations


@app.route('/')
def index():
    return 'hello'


@app.route('/recommendations', methods=['GET'])
def recommendations_handler():
    sku = request.args.get('sku', type=str)
    threshold = request.args.get('min_threshold', type=float)
    if sku:
        try:
            data = app.config['DATA']
            recommendations = get_recommendations(data=data, sku=sku, min_threshold=threshold)
            return jsonify(sku=sku, recommendations=recommendations)
        except Exception as err:
            app.logger.error(err)
            return make_response(jsonify(error='Unexpected error', status=500), 500)
    return make_response(jsonify(error='Parameter "sku" is required ', status=400), 400)
