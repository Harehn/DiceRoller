from flask import Flask, request, send_file
from flask_cors import CORS
from random import random, randint
import helper
from roller import evaluate, parse

app = Flask(__name__)
CORS(app)


@app.route("/")
def homepage():
    import os
    path = os.getcwd() + '/homepage.html'
    if app.debug:
        path = os.getcwd() + '/Backend/homepage.html'
    return helper.get_file(path)


@app.route("/roll", methods=['GET'])
def roll():
    dice = None
    if request.method == 'GET':
        dice = request.args["roll"]
    # return f"<h1>This is the roll: {roll_dice(dice)}</h1>"
    return {'result': evaluate(dice)}


def roll_dice(dice):
    return (randint(1, int(dice)))


@app.route("/wake")
def wake():
    return {'message': 'Backend is now awake.'}


@app.route("/dev")
def in_dev():
    import os
    return "App in development mode" if app.debug else "App in Production mode"

@app.route("/doc")
def doc():
    filename = "test.txt"
    import os
    path = os.getcwd() + filename
    if app.debug:
        path = os.getcwd() + filename
    try:
        with open(path, 'w') as in_file:
            in_file.write("Just having a great time.")
        return send_file(path)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # app.run(debug=True) # DEVELOPMENT MODE
    app.run(host='0.0.0.0', port=3000) # PRODUCTION MODE
