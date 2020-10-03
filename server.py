import sys
from json import dumps
from flask import Flask, request
import emissions
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

@APP.route('/home/emissions', methods=['POST'])
def calculate_emissions():
    data = request.get_json()
    output = emissions.emissions(data['distance_travelled'], data['make'], data['vehicle_class'])

    return dumps(output)
    

if __name__ == "__main__":
    APP.run(port=(int(sys.argv[1]) if len(sys.argv) == 2 else 8080))

