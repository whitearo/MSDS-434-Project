# !/usr/bin/env python
# Copyright 2018 Google LLC
# batch update bigquery from imported csv

# [START gae_python37_app]
from flask import Flask
from google.cloud import bigquery
#from google.appengine.ext import webapp
#from google.appengine.ext.webapp import util


app = Flask(__name__)


@app.route('/')
def root():
    #application = webapp.WSGIApplication([('/', MyHandler)], debug=True)
    #util.run_wsgi_app(application)
    #x = MyHandler()
    #return x.get() 
    return "hello world"


class MyHandler(webapp.RequestHandler):
    def get(self):
        #housing_units = self.request.get_all("housing_units")
        #median_income = self.request.get_all("median_income")
        #self.response.out.write(housing_units + ',' + median_income)
        return "parameters:" #+ housing_units + ',' + median_income


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
    #root()
# [END gae_python37_app]
