# Standard library modules
from crypt import methods
import logging
import sys
import time

# Installed packages
from flask import Blueprint
from flask import Flask
from flask import request
from flask import Response

from prometheus_flask_exporter import PrometheusMetrics

import requests

import simplejson as json
import jwt 
# The application

app = Flask(__name__)

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'User process')

bp = Blueprint('app', __name__)

db = {
    "name": "http://trocketdb:30002/api/v1/datastore",
    "endpoint": [
        "hello_world",
        "create_playlist",
        "update_playlist",
        "delete_playlist",
        "connect_to_db",
        "get_username",
        "authenticate_user"
    ]
}


@bp.route('/', methods=['GET'])
@metrics.do_not_track()
def hello_world():
    return ("If you are reading this in a browser, your service is "
            "operational. Switch to curl/Postman/etc to interact using the "
            "other HTTP verbs.")


@bp.route('/health')
@metrics.do_not_track()
def health():
    return Response("", status=200, mimetype="application/json")


@bp.route('/readiness')
@metrics.do_not_track()
def readiness():
    return Response("", status=200, mimetype="application/json")

@bp.route('/', methods = ['POST'])
def create_playlist():
    """
    Create the playlist for the user
    """

@bp.route('/<user_id>', methods = ['PUT'])
def update_playlist():
    """
    Update the playlist of the current user
    """
    
@bp.route('/<user_id>', methods = ['DELETE'])
def delete_playlist():
    """
    Delete the playlist of the current user
    """
    
@bp.route('/', methods = ['GET'])
def connect_to_db():
    """
    Connect to the DB
    """

@bp.route('/<user_id>', methods = ['GET'])
def get_username():
    """
    Get the username of the current user
    """

@bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    headers = request.headers
    # check header here
    if 'Authorization' not in headers:
        return Response(
            json.dumps({"error": "missing auth"}),
            status=401,
            mimetype='application/json')
    payload = {"objtype": "user", "objkey": user_id}
    url = db['name'] + '/' + db['endpoint'][0]
    response = requests.get(url, params=payload)
    return (response.json())

@bp.route('/login', methods=['PUT'])
def login():
    try:
        content = request.get_json()
        uid = content['uid']
    except Exception:
        return json.dumps({"message": "error reading parameters"})
    url = db['name'] + '/' + db['endpoint'][0]
    response = requests.get(url, params={"objtype": "user", "objkey": uid})
    data = response.json()
    if len(data['Items']) > 0:
        encoded = jwt.encode({'user_id': uid, 'time': time.time()},
                             'secret',
                             algorithm='HS256')
    return encoded


@bp.route('/logoff', methods=['PUT'])
def logoff():
    try:
        content = request.get_json()
        _ = content['jwt']
    except Exception:
        return json.dumps({"message": "error reading parameters"})
    return {}

# All database calls will have this prefix.  Prometheus metric
# calls will not---they will have route '/metrics'.  This is
# the conventional organization.
app.register_blueprint(bp, url_prefix='/api/v1/playlist/')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.error("Usage: app.py <service-port>")
        sys.exit(-1)

    p = int(sys.argv[1])
    # Do not set debug=True---that will disable the Prometheus metrics
    app.run(host='0.0.0.0', port=p, threaded=True)