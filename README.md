# Overview
This is a nutrition chatbot that gives factual information surrounding food and dietary routines.

# Content List
- [Installation](https://github.com/iphonexsmax25/-Midori-No-Kaze-/blob/main/README.md#installation)
- [How to Use](https://github.com/iphonexsmax25/-Midori-No-Kaze-/blob/main/README.md#how-to-use)
- [File Description](https://github.com/iphonexsmax25/-Midori-No-Kaze-/blob/main/README.md#file-description)

# Installation
1. This step will take multiple package installations. This is how to install packages on Windows (other OS is currently not supported):
```
pip install [PACKAGE]
```

2. Clone this repository.

3. Inside the app directory, initiate a virtual environment ```env``` to store variables and dependencies inside:
```
python -m venv .env
.env\Scripts\activate
```

4. Install the following packages:
    - ```markdown``` to convert a markdown text into HTML.
    - ```flask``` to run a local server, hosting the application.
    - ```requests``` to initiate HTTP requests for API call.

5. Sign up/sign in on ```ollama.com```, and get the api key.

6. Under the ```static``` directory, add a new file ```ollama_info.py``` and type inside:
```
KEY = "[Insert your API Key here]"
MODEL = "gpt-oss:120b-cloud"
```

Now you can use the chatbot!

# How to Use
Run ```main.py``` in your IDE, or open a terminal in the current directory and run:
```
python .\main.py
```

This will run the server on the terminal and open a page in your browser.

# File Description
The file ```main.py``` and everything inside ```static``` and ```templates``` directories construct the application. Everything else is implicit or for testing purposes only.

- ```main.py``` is the main program, which may contain input processing.
- ```templates/``` is the directory containing the user interface, written with Flask Jinja in mind.
- ```static/chatbot.css``` is a style sheet.
- ```static/interface.js``` is a script that extracts user input and displays dialogs.
- ```static/process_prompt.py``` is the module that processes user input into a bot response.
