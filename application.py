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
        return make_response('Predictchurrisk API here'})

@app.route('/dam/predictsegment', methods=['POST'])
def dampredictsegment():
    if request.method == "POST":
        content = request.get_json()
        df = pd.io.json.json_normalize(content)
        return 'API Response here, can be json'

@app.route('/dam/predictchurnrisk', methods=['POST'])
def dampredictchurnrisk():
    if request.method == "POST":
        if request.authorization:
            username = request.authorization.username
            password = request.authorization.password
        else:
            return make_response('Basic Authentication not provided', 401, {'WWW-Authenticate': 'Basic-realm="Login Required"'})

        if username != "khanmaaz" or password != "mypassword":
            return make_response('Incorrect Basic Authentication', 401, {'WWW-Authenticate' : 'Basic-realm="Login Required"'})

        content = request.get_json()
        inputdf = pd.io.json.json_normalize(content)
        noofrecs = inputdf.count()

        return 'No of records is ' + str(noofrecs)

if __name__ == '__main__':
    app.run()

