import sys
from json import dumps
from flask import Flask, request
from emissions import calc_co2, calc_co
from fossilfuels import get_fossilfuels
from get_s5obs import get_s5obs
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

@APP.route('/', methods=['POST'])
def calculate_emissions():

    make               = request.form['make']
    distance_travelled = request.form['distance_travelled']
    vehicle_class      = request.form['vehicle_class']

    longitude          = request.form['longitude']
    latitude           = request.form['latitude']
    start              = request.form['start']
    end                = request.form['end']
        
    co2 = calc_co2(float(distance_travelled), make, vehicle_class)
    co = calc_co(float(distance_travelled), make, vehicle_class)
        
    fossilfuelco2 = get_fossilfuels(float(longitude), float(latitude), start)
    co_observed = get_s5obs(float(longitude), float(latitude), start, end)
        
    output = {"CO2 emissions":co2, "CO emissions":co, "CO2 fossil fuel observation":fossilfuelco2, "CO observed":co_observed}

    return dumps(output)


if __name__ == "__main__":
    APP.run(debug=True, port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8080))

