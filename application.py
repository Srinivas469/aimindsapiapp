import flask
from flask import request, url_for, jsonify, make_response
import pandas as pd


app = flask.Flask(__name__)


@app.route('/')
def allapidetails():
    return "Below are the list of Model APIs that can be used!"


@app.route('/jum/predictchurnrisk', methods=['POST'])
def jumpredictchurnrisk():
    if request.method == "POST":
        #All API Logic here
        return 'Predictchurrisk API here'


if __name__ == '__main__':
    app.run()

