import os
import webbrowser
from random import random
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"Access-Control-Allow-Origin": "file:///E:/Python%20Project/HACKATHON/SIM_UOL%20CSSC%202025/-Midori-No-Kaze-/index.html"}})


@app.route('/')
def process():
    return "Test"

@app.route('/rand/')
@cross_origin() # Enables CORS for this specific route
def random_num():
    return f"{random():.2%}"

def main():
    # webbrowser.open("index.html")
    app.run(host = "localhost", port = 8000, debug = True)

if __name__ == '__main__':
    main()