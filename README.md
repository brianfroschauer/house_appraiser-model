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
Response example:
```json
{
  "price": 500000
}
```

#### Get all zones
Method: GET

URL: http://127.0.0.1:5000/zones

Response example:
```json
[
  "Pilar",
  "Nordelta",
  "San Isidro"
]
```

#### Get price in function of the total or covered surface

Method: GET

URL: http://127.0.0.1:5000/prices

Params:
1. surface: ['covered', 'total']

Response example:
```json
[
  {
	"total_surface": 400,
	"average_price": 500000
  },
  {
	"total_surface": 500,
	"average_price": 600000
  }
]
```

#### Get amount of houses by zone

Method: GET

URL: http://127.0.0.1:5000/houses

Response example:
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

URL: http://127.0.0.1:5000/prices/by-zone/average

Params:
1. range: ['asc', 'desc']
2. top: number

Response example:
```json
[
  {
    "zone": "Pilar",
	"average_price": 150000
  },
  {
    "zone": "Nordelta",
	"average_price": 300000
  }
]
```

#### Average price by bathrooms amount

Method: GET

URL: http://127.0.0.1:5000/prices/by-bathrooms

Response example:
```json
[
  {
    "bathrooms": 1,
	"average_price": 150000
  },
  {
    "zone": 3,
	"average_price": 300000
  }
]
```

#### Prices by zone

Method: GET

URL: http://127.0.0.1:5000/prices/by-zone/average

Response example:
```json
[
    {
        "amount": 22,
        "class": 0,
        "zone": "Almirante Brown"
    },
    {
        "amount": 23,
        "class": 1,
        "zone": "Almirante Brown"
    }
]
```
