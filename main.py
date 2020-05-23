from flask import Flask, jsonify, request

from flask_cors import CORS

from model import predict, find_zone, find_all_zones, price_by_total_surface, houses_by_zone, avg_price_by_zone

app = Flask(__name__)
CORS(app)


@app.route('/prices', methods=['GET'])
def prices():
    surface = request.args.get('surface')

    if surface is None:
        return []

    surface = surface + '_surface'

    result = list(map(lambda t: {surface: int(t[0]), 'average_price': int(t[1])}, price_by_total_surface(surface)))
    return jsonify(result)


@app.route('/houses', methods=['GET'])
def houses():
    zone = request.args.get('zone')
    count = houses_by_zone(zone)
    return jsonify(zone=zone, amount=count)


@app.route('/zones', methods=['GET'])
def zones():
    return jsonify(find_all_zones())


@app.route('/prices/by-zone', methods=['GET'])
def price_by_zone():
    range = request.args.get('range')
    top = int(request.args.get('top'))
    result = list(map(lambda t: {'zone': t[0], 'average_price': int(t[1])}, avg_price_by_zone(range, top)))
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
