import os, signal
import webbrowser
from random import random, randint
from flask import Flask, render_template, url_for, request
from flask_cors import cross_origin
from requests import get
from json import loads

app = Flask(__name__)

@app.route('/reply/', methods = ["POST"])
# @cross_origin() # Enables CORS for this specific route
def process_user_input():
    try:
        prompt = bytes.decode(request.data)
        r = get("https://randomfox.ca/floof")
        d: dict[str, str] = loads(r.content)
        return prompt[::-1] + f" {random():.1%}<br><img src='{d['image']}' height=128>"
    except Exception as e:
        return f"I can't reason well. {e}"

@app.route('/terminate/')
def terminate():
    os.kill(os.getpid(), signal.SIGINT)
    return ""

@app.route('/')
def index():
    return render_template('index.html')

def main():
    if not os.environ.get("FLASK_INITIALIZED"):
        webbrowser.open("http://localhost:8000")    
        os.environ["FLASK_INITIALIZED"] = "1"
    app.run(host = "localhost", port = 8000, debug = True)

if __name__ == '__main__':
    main()