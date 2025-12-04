import os, signal, webbrowser, static.process_prompt as pp
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/reply/', methods = ["POST"])
def process_user_input():
    try:
        prompt = bytes.decode(request.data)
        return pp.process(prompt)
    except Exception as e:
        return f"<p>I cannot fetch your answer right now. Please restart this application.</p>"

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