from flask import Flask, jsonify, request

# Data analysis modules
import pandas as pd
from flask_cors import CORS

from sklearn.model_selection import train_test_split

# Fit model modules
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)

zone_dict = {}


@app.route('/predict', methods=['POST'])
def linear_regression():
    model = train_model()

    total_surface = request.json['total_surface']
    covered_surface = request.json['covered_surface']
    rooms = request.json['rooms']
    bathrooms = request.json['bathrooms']
    garages = request.json['garages']
    bedrooms = request.json['bedrooms']
    toilettes = request.json['toilettes']
    antiquity = request.json['antiquity']
    zone = zone_dict.get(request.json['zone'])

    if zone is None:
        return jsonify(error="Zone, " + request.json['zone'] + ", is not found")

    feature = [[total_surface, covered_surface, rooms, bathrooms, garages, bedrooms, toilettes, antiquity, zone]]

    prediction = model.predict(feature)[0]

    return jsonify(price=round(prediction))


def train_model():
    train = pd.read_csv('./dataset/dataset.csv')

    init_zone_dict(train)

    # Split dataset into “x” features and “y” labels
    x = train[[
        'total_surface',
        'covered_surface',
        'rooms',
        'bathrooms',
        'garages',
        'bedrooms',
        'toilettes',
        'antiquity',
        'zone_label'
    ]]

    y = train['price']

    x_train, x_test, y_train, y_test = train_test_split(x, y)

    # Create instance of LogisticRegression
    model = LinearRegression()

    # Fit the model using the training data
    # X_train -> parameter supplies the data features
    # y_train -> parameter supplies the target labels
    model.fit(x_train, y_train)

    return model


def init_zone_dict(train):
    for i in range(len(train)):
        zone_dict[train['zone'][i]] = train['zone_label'][i]