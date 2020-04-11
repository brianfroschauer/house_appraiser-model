from flask import Flask, jsonify, request

# Data analysis modules
import pandas as pd

from sklearn.model_selection import train_test_split

# Fit model modules
from sklearn.linear_model import LinearRegression

app = Flask(__name__)


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

    feature = [[total_surface, covered_surface, rooms, bathrooms, garages, bedrooms, toilettes, antiquity]]

    prediction = model.predict(feature)[0]

    return jsonify(price=round(prediction))


def train_model():
    train = pd.read_csv('./dataset/dataset.csv')

    # Split dataset into “x” features and “y” labels
    x = train[[
        'total_surface',
        'covered_surface',
        'rooms',
        'bathrooms',
        'garages',
        'bedrooms',
        'toilettes',
        'antiquity'
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
