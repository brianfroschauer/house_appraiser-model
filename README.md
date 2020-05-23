# House Appraiser

## Machine Learning Model

Linear regression developed with sklearn to predict the value of a property based on certain features.

## Usage

Run the application using:

```bash
$ export FLASK_APP=main.py
$ flask run
```

### API

#### Predict price

Method: POST

URL: http://127.0.0.1:5000/predict

Payload:
```json
{
    "total_surface": 400,
    "covered_surface": 200,
    "rooms": 6,
    "bathrooms": 2,
    "garages": 0,
    "bedrooms": 2,
    "toilettes": 2,
    "antiquity": 0,
    "zone": "Pilar"
}
```

#### Get price in function of the total or covered surface

Method: GET

URL: http://127.0.0.1:5000/prices

Params:
1. surface: ['covered', 'total']

Payload:
```json
[
  {
	"total_surface": 400,
	"average_price": 500.000
  },
  {
	"total_surface": 500,
	"average_price": 600.000
  }
]
```

#### Get amount of houses by zone

Method: GET

URL: http://127.0.0.1:5000/houses

Params:
1. zone: zone string

Payload:
```json
[
  {
	"zone": "Pilar",
	"amount": 328
  },
  {
	"zone": "Nordelta",
	"amount": 200
  }
]

```

#### Average price by zone

Method: GET

URL: http://127.0.0.1:5000/prices/by-zone

Params:
1. range: ['asc', 'desc']
2. top: number

Payload:
```json
[
  {
    "zone": "Pilar",
	"average_price": 150.000
  },
  {
    "zone": "Nordelta",
	"average_price": 300.000
  }
]
```
