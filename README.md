# House Appraiser

## Machine Learning Model

Linear regression developed with sklearn to predict the value of a property based on certain features.

## Usage

Run the application using:

```bash
$ export FLASK_APP=main.py
$ flask run
```

### Request

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

### Response
```json
{
    "price": 400000
}
```
