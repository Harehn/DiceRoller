from flask import Flask, request
from flask_cors import CORS
from random import random, randint
import helper

app = Flask(__name__)
CORS(app)


@app.route("/")
def homepage():
    import os
    return os.getcwd()
    # return "<h1>This is the homepage</h1>"
    # path = 'C:/Users/Vivek/PycharmProjects/DiceRoller/Backend/homepage.html'
    #return helper.get_file('Backend/homepage.html')


@app.route("/roll", methods=['GET'])
def roll():
    dice = None
    if request.method == 'GET':
        dice = request.args["roll"]
    # return f"<h1>This is the roll: {roll_dice(dice)}</h1>"
    return {'result': roll_dice(dice)}


def roll_dice(dice):
    return (randint(1, int(dice)))


if __name__ == "__main__":
    # CHANGED to PRODCUCTION MODE
    # app.run(debug=True)
    app.run()

