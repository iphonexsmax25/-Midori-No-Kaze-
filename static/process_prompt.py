from typing import Any
from random import random, randint
from requests import get
from json import loads

# HTML Attributes
def compile_attributes(**attributes: Any) -> str:
    att_pairs: list[str] = []
    for key, value in attributes.items():
        att_pairs.append(f"{key}={value}")
    return " ".join(att_pairs)

# HTML Element
def hyperlink(url: str, text: str|None = None, **attributes: Any) -> str:
    return f"<a href=\"{url}\" {compile_attributes(**attributes)}>{text if text else url}</a>"

def image(source: str, **attributes: Any) -> str:
    return f"<img src='{source}' {compile_attributes(**attributes)}>"

def encase(element: str, text: str) -> str:
    return f"<{element}>{text}</{element}>"

def plaintext(text: str) -> str:
    return text.replace("&", '&amp;').replace("<", '&lt;').replace(">", '&gt;')

# Presets
def preset_1(prompt: str) -> str:
    r = get("https://randomfox.ca/floof")
    d: dict[str, str] = loads(r.content)
    return f"{encase("p", plaintext(prompt[::-1]) + " " + encase("b", f"{random():.1%}"))} <br>{image(d['image'], height = 128)}<br>{hyperlink(d['image'], style = "color:red")}"

def preset_2(prompt: str) -> str:
    cat_gif = image("https://cataas.com/cat/gif", height = 128)
    cat_fact_resp = get("https://meowfacts.herokuapp.com/")
    cat_fact: str = loads(cat_fact_resp.content)['data'][0]
    return encase("h1", "Cat Facts!") + cat_gif + encase("p", cat_fact)
    

# Main Process
def process(prompt: str) -> str:
    return preset_1(prompt)

def main():
    print(process("Get me an ice cream!"))
if __name__ == '__main__':
    main()