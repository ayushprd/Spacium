import sys
from json import dumps
from flask import Flask, request
from emissions import calc_co2, calc_co
import json


def defaulthandler(err):
    """
    error handling
    """
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response
APP = Flask(__name__)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaulthandler)

@APP.route('/', methods=['POST', 'GET'])
def calculate_emissions():
    if request.method == 'POST':

        make = request.form['make']
        distance_travelled = request.form['distance_travelled']
        vehicle_class = request.form['vehicle_class']

        co2 = calc_co2(float(distance_travelled), make, vehicle_class)
        co = calc_co(float(distance_travelled), make, vehicle_class)

        output = {"CO2 emissions":co2, "CO emissions":co}

        return dumps(output)

    else:
        return("Our home page goes here")

if __name__ == "__main__":
    APP.run(debug=True, port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8080))

