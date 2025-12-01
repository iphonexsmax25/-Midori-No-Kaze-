import webbrowser
from random import random, randint
from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/reply/<prompt>')
@cross_origin() # Enables CORS for this specific route
def process_user_input(prompt):
    return prompt[::-1]

def main():
    webbrowser.open("index.html")
    app.run(host = "localhost", port = 8000, debug = True)

if __name__ == '__main__':
    main()