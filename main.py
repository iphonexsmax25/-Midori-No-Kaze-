import webbrowser
from random import random, randint
from flask import Flask
from flask_cors import cross_origin
from requests import get
from json import loads

app = Flask(__name__)

@app.route('/reply/<prompt>')
@cross_origin() # Enables CORS for this specific route
def process_user_input(prompt):
    r = get("https://randomfox.ca/floof")
    d: dict[str, str] = loads(r.content)
    return prompt[::-1] + f"<br><img src='{d['image']}' height=128>"

def main():
    # webbrowser.open("index.html")
    app.run(host = "localhost", port = 8000, debug = True)

if __name__ == '__main__':
    main()