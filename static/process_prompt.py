from typing import Any
from random import random, randint
from requests import get
from json import loads

def compile_attributes(**attributes: Any) -> str:
    att_pairs: list[str] = []
    for key, value in attributes.items():
        att_pairs.append(f"{key}={value}")
    return " ".join(att_pairs)

def hyperlink(url: str, text: str|None = None, **attributes: Any) -> str:
    return f"<a href=\"{url}\" {compile_attributes(**attributes)}>{text if text else url}</a>"

def image(source: str, **attributes: Any) -> str:
    return f"<img src='{source}' {compile_attributes(**attributes)}>"

def process(prompt: str) -> str:
    r = get("https://randomfox.ca/floof")
    d: dict[str, str] = loads(r.content)
    return \
        prompt[::-1] + f" {random():.1%}<br>\
        {image(d['image'], height = 128)}<br>\
        {hyperlink(d['image'], style = "color:red")}"

def main():
    pass
if __name__ == '__main__':
    main()