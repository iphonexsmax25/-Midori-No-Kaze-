from typing import Any
from random import random, randint
from requests import get, post
from json import loads, dumps
import markdown
from static.ollama_info import *

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

def build_table(text: str) -> str:
    result: list[str] = []
    in_table: bool = False
    header: bool = False
    for line in text.split("\n"):
        # print(result[-1] if result else "")
        # print(f"\t{in_table=}\n\t{header=}")
        if in_table and "|-" in line:
            continue

        if line.startswith("<p>| "):
            result.append("<table>")
            in_table = True
            header = True
            line = line[3:]

        if not in_table:
            result.append(line)
            continue

        if in_table and line.endswith(" |</p>"):
            in_table = False
            line = line[:-4]

        # Found start of table, parse.
        cols: list[str] = [x.strip() for x in line[1:-1].split("|")]

        if header:
            elements: list[str] = [f"<th>{x}</th>" for x in cols]
            header = False
        else:
            elements: list[str] = [f"<td>{x}</td>" for x in cols]

        # Add Row
        result.append("<tr>\n" + "\n".join(elements) + "\n</tr>")

        # Add end of table tag
        if not in_table:
            result.append("</table>")
    return "\n".join(result)


# Presets
def preset_0(prompt: str) -> str:
    """
    Identity process.
    
    :param prompt: user input
    :type prompt: str
    :return: bot response
    :rtype: str
    """
    return encase("p", f"process({prompt})")

def preset_1(prompt: str) -> str:
    r = get("https://randomfox.ca/floof")
    d: dict[str, str] = loads(r.content)
    return f"{encase("p", plaintext(prompt[::-1]) + " " + encase("b", f"{random():.1%}"))} <br>{image(d['image'], height = 128)}<br>{hyperlink(d['image'], style = "color:red")}"

def preset_2(prompt: str) -> str:
    cat_gif = image("https://cataas.com/cat/gif", height = 128)
    cat_fact_resp = get("https://meowfacts.herokuapp.com/")
    cat_fact: str = loads(cat_fact_resp.content)['data'][0]
    return encase("h1", "Cat Facts!") + cat_gif + encase("p", cat_fact)

def preset_3(prompt: str) -> str:
    # Reference: https://docs.ollama.com/api/introduction
    req_payload = {
        "model": "gpt-oss:120b-cloud", 
        "prompt": "Respond in under 300 words. I am living in Singapore. Do not mention this and the previous statement. " + prompt,
        "stream": False,

        }
    response = post(
        "https://ollama.com/api/generate", 
        headers={"Authorization": f"Bearer {KEY}"},  # Key is omitted for security purpose
        json=req_payload)
    # response = ollama.chat(model='gpt-oss:120b-cloud', messages=[{
    #     'role': 'user',
    #     'content': prompt
    # }])
    res_payload = loads(response.content)
    
    return markdown.markdown(res_payload['response'], output_format = "html")

def preset_4(prompt: str) -> str:
    return build_table(anyeong)

# Main Process
def process(prompt: str) -> str:
    try:
        return preset_4(prompt)
    except Exception as e:
        print(e)
        return "I can't respond right now."

def main():
    # print(os.getenv("OLLAMA_API_KEY"))
    # print(process("Get me an ice cream!"))

#     table_str = \
# """<p>Carbohydrates often get a bad rap, but they’re not inherently “bad.” Whether carbs help or hinder your health depends on several factors, including the type of carbohydrate, the amount you eat, and the context of your overall diet and lifestyle.</p>
# <h3>1. Types of Carbohydrates</h3>
# <p>| Category | What it includes | Typical impact |
# |---|---|---|
# | <strong>Simple carbs</strong> | Sugars found in fruit, honey, table sugar, candy, sodas, pastries | Quickly raise blood glucose; can cause spikes in energy followed by crashes if consumed in excess, especially when they’re refined (e.g., white sugar, corn syrup). |
# | <strong>Complex carbs</strong> | Starches and fiber in whole grains, legumes, tubers, vegetables | Digest more slowly, provide sustained energy, and often come with vitamins, minerals, and fiber that support digestion and heart health. |
# | <strong>Resistant starch &amp; fiber</strong> | Certain legumes, cooled potatoes/rice, oats, barley, chia seeds | Ferment in the colon, feeding beneficial gut bacteria and improving blood‑sugar control. |</p>
# <p><em>Bottom line:</em> <strong>Whole, minimally processed carbs</strong> (whole grains, legumes, fruits, vegetables) are generally beneficial, whereas <strong>refined, sugary carbs</strong> (white bread, pastries, sugary drinks) are the ones most associated with negative health outcomes.</p>
# <h3>2. How Carbs Influence Your Body</h3>"""
#     print(build_table(table_str))
    # with open("static/test.html", "w") as file:
    #     print(anyeong[:50])
    #     for char in build_table(anyeong):
    #         try:
    #             file.write(char)
    #         except Exception as e:
    #             file.write("?")
    print(build_table(anyeong))
if __name__ == '__main__':
    main()

