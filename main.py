from flask import Flask, jsonify, request

from flask_cors import CORS

from model import predict, find_zone, find_all_zones, price_by_total_surface

app = Flask(__name__)
CORS(app)


@app.route('/zones', methods=['GET'])
def all_zones():
    surface = request.args.get('surface')

    if surface is None:
        return jsonify(zones=find_all_zones())

    surface = surface + '_surface'

    result = list(map(lambda t: {surface: int(t[0]), 'average_price': int(t[1])}, price_by_total_surface(surface)))
    return jsonify(result)


@app.route('/predict', methods=['POST'])
def linear_regression():
    total_surface = request.json['total_surface']
    covered_surface = request.json['covered_surface']
    rooms = request.json['rooms']
    bathrooms = request.json['bathrooms']
    garages = request.json['garages']
    bedrooms = request.json['bedrooms']
    toilettes = request.json['toilettes']
    antiquity = request.json['antiquity']
    zone = find_zone(request.json['zone'])

    if zone is None:
        return jsonify(error="Zone, " + request.json['zone'] + ", is not found")

    feature = [[total_surface, covered_surface, rooms, bathrooms, garages, bedrooms, toilettes, antiquity, zone]]
    prediction = predict(feature)

    return jsonify(price=prediction)
