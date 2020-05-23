# Data analysis modules
import pandas as pd

# Scikit learn modules
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

clf = LinearRegression()
zones = {}

data = pd.read_csv('./dataset/dataset.csv')

# Create dict of all zones
for i in range(len(data)):
    zones[data['zone'][i]] = data['zone_label'][i]

# Split dataset into “x” features and “y” labels
x = data[[
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

y = data['price']

x_train, x_test, y_train, y_test = train_test_split(x, y)

# Fit the classifier using the training data
# X_train -> parameter supplies the data features
# y_train -> parameter supplies the target labels
clf.fit(x_train, y_train)


def predict(feature):
    return round(clf.predict(feature)[0])


def find_all_zones():
    return [*zones]


def find_zone(zone):
    return zones.get(zone)


def price_by_total_surface(surface):
    if surface != 'covered_surface' and surface != 'total_surface':
        return []

    ordered_data = data.sort_values(by=[surface])
    ordered_data = ordered_data.drop(
        ['covered_surface' if surface == 'total_surface' else 'total_surface',
         'rooms',
         'bathrooms',
         'garages',
         'bedrooms',
         'toilettes',
         'antiquity',
         'zone',
         'zone_label',
         'index',
         ], axis=1)

    print('ordered_data')
    print(ordered_data)

    grouped_data = ordered_data.groupby([surface]).mean().reset_index()

    return list(map(tuple, grouped_data.to_numpy()))
