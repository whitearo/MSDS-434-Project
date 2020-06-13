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
    gcs_uri = 'gs://msds-434-project-275301/sources/real_estate_sample.json'
    dataset_ref = client.dataset('real_estate_analysis')
    job_config = bigquery.job.LoadJobConfig()
    job_config.schema = [
        bigquery.SchemaField('ListID', 'INTEGER'),
        bigquery.SchemaField('Address', 'STRING'),
        bigquery.SchemaField('City', 'STRING'),
        bigquery.SchemaField('State', 'STRING'),
        bigquery.SchemaField('Price', 'INTEGER'),
    ]
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    # Import data files from cloud storage buckets
    load_job = client.load_table_from_uri(
        gcs_uri,
        dataset_ref.table('sample'),
        job_config=job_config,
    )

    print("Starting job {}".format(load_job.job_id))
    load_job.result()  # Waits for table load to complete.

    # destination_table = client.get_table(dataset_ref.table("sample"))
    # print("Loaded {} rows.".format(destination_table.num_rows))
    return 'Job finished'


if __name__ == '__updatebq__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
