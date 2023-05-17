from flask import Flask
from models.GPS import GPS

app = Flask(__name__)


@app.route("/")
def hello_world():
    cords = GPS.read_coordinates()
    status_code = 200
    if cords['latitude'] == 0 or cords['longitude'] == 0:
        status_code = 503
    response = {
        "coordinates": cords,
        "status_code": status_code,
        "mimetype": 'application/json'
    }
    return response
