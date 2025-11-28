from flask import Flask
from requests import get
from json import loads
import webbrowser

INDEX_HTML: str = "testing\\index.html"

# app = Flask(__name__)

# @app.route('/')
def hello_world():
    """
    This function, when called, sends an HTTP GET request to the API to fetch a random fox image.
    This only serves as a placeholder/test function.
    """
    r = get("https://randomfox.ca/floof")
    d: dict[str, str] = loads(r.content)
    image: str = d['image']

    # Read the content of index.html
    index_content: str = ""
    with open(INDEX_HTML) as file:
        index_content = file.read()

    # Change line 13 (image) by rewriting all content, except the image line.
    with open(INDEX_HTML, "w") as file:
        for line in index_content.split("\n"):
            if "<img class=\"fox\"" in line:
                file.write(f"  <img class=\"fox\" src=\"{image}\" height=512>\n")
            else:
                file.write(line + "\n")
            

def process_response(response: str) -> str:
    """
    Process the end-user's response.
    This serves as a placeholder.

    :param response: The end-user's input in the chat.
    :type response: str
    :return: The bot's response.
    :rtype: str
    """
    return response[::-1].upper()

def main():
    # user_input: str = input("Chat: ")
    # reply: str = process_response(user_input)
    # print("Bot:", reply)
    # app.run()
    hello_world()
    webbrowser.open("testing\\index.html")
if __name__ == "__main__":
    main()