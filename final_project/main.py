# !/usr/bin/env python
# Copyright 2018 Google LLC
# batch update bigquery from imported csv

# [START gae_python37_app]
from flask import Flask
#from google.cloud import bigquery

app = Flask(__name__)


@app.route('/')
def root():
    message = request.get_json().get('message', '')
    return jsonify({'message': message})


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
