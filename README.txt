1. pip3 install flask
2. import flask
from flask import Flask, jsonify
3. instantiate flask
my_app = Flask("My first app")
@my_app.route('/')
def hello_world():
    return 'Hello world'
if name == "main":
    my_app.run(debug=True)

4. run the application
flask --app server --debug run

5. access the endpoint(FROM GIT BASH NOT POWERSHELL)
curl -X GET -i -w '\n' localhost:5000


can also import render_template and request from flask

