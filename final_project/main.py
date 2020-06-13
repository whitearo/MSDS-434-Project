# !/usr/bin/env python
# Copyright 2018 Google LLC
# batch update bigquery from imported csv

# [START gae_python37_app]
from flask import Flask
from google.cloud import bigquery


app = Flask(__name__)


@app.route('/')
def update_bigquery():
    # Create bigquery connection
    client = bigquery.Client()
    # Set up data to be imported
    # Perform a query.
    QUERY = (
        'SELECT source.price, predicted_price, \
            results.place_name, results.floor, \
            results.rooms, results.surface_total, results.surface_covered \
        FROM \
            `msds-434-project-275301.real_estate_analysis.br_201501` AS source\
        INNER JOIN \
        ML.PREDICT(MODEL `real_estate_analysis.properties_br_model`,\
        (\
            SELECT id, place_name, \
                IFNULL(floor,0) AS floor, \
                IFNULL(rooms,0) AS rooms, \
                IFNULL(surface_total,0) AS surface_total, \
                IFNULL(surface_covered,0) AS surface_covered \
            FROM `msds-434-project-275301.real_estate_analysis.br_201501`\
            WHERE price > 0 \
                AND floor > 0 AND rooms > 0 \
                AND surface_total > 0 \
                AND surface_covered > 0)) AS results \
        ON source.id = results.id')

    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    json_result = ''
    for row in rows:
        json_result = json_result + '{\n\"Price\":' + str(row.price) + ',\n' + \
                      '\"Predicted_price\":' + str(row.predicted_price) + ',\n' + \
                      '\"Floor\":' + str(row.floor) + ',\n' + \
                      '\"Rooms\":' + str(row.rooms) + ',\n' + \
                      '\"Place_name\":' + row.place_name + '\n}' + '\n'
        break
    return json_result


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
