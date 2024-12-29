from flask import Flask, request
from flask_cors import CORS
from random import random, randint
import helper
from roller import evaluate,parse

app = Flask(__name__)
CORS(app)


@app.route("/")
def homepage():
    import os
    path = os.getcwd() + '/homepage.html'
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


if __name__ == "__main__":
    # CHANGED to PRODCUCTION MODE
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=3000)

