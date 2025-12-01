import webbrowser
from random import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def process():
    return "Test"

@app.route('/rand/')
def random_num():
    return f"{random():.2%}"

def main():
    webbrowser.open("index.html")
    app.run(host = "localhost", port = 8000, debug = True)

if __name__ == '__main__':
    main()