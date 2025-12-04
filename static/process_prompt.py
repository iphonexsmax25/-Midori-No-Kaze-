from typing import Any
import requests, markdown, json
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
        result.append("<tr>" + "".join(elements) + "</tr>")

        # Add end of table tag
        if not in_table:
            result.append("</table>")
    return "".join(result)


# Presets
def has_alpha(text: str) -> bool:
    for char in text:
        if char.isalpha():
            return True
    return False

def lorem_ipsum(prompt: str) -> str:
    """Lorem ipsum for testing."""
    r = requests.get("http://metaphorpsum.com/paragraphs/4", params = {"p": True})
    print(r)
    texts: str = r.content.decode()
    # print(texts)
    paras: list[str] = [line for line in texts.split("\n") if has_alpha(line)]
    result: str = "".join(paras)
    print(result)
    return result

def get_ai_response(prompt: str) -> str:
    """
    Use Ollama's AI model to process prompt into a useful response.
    
    :param prompt: user input
    :type prompt: str
    :return: bot response
    :rtype: str
    """
    # Rules are used to constrain the prompt.
    RULES: list[str] = [
        "I am living in Singapore.",
        "When I ask a question, consider the perspective of the opposing view and state why it may or may not be the feasible solution.", # To strengthen argument by providing unbiased view.
        "Respond and paraphrase in a friendly and informal tone, in under 300 words.",
<<<<<<< HEAD
        "Do not mention this and the previous statement in your response.",
        "Now, answer the following question: "
=======
        "Do not mention this and the previous statement and answer the following question: "
>>>>>>> 9c3a571302cdcd0e539eca7b3ef027a08dcba2a7
    ]
    # Reference: https://docs.ollama.com/api/introduction
    req_payload = {
        "model": "gpt-oss:120b-cloud", 
        "prompt": " ".join(RULES + [prompt]),
        "stream": False,
        }
    
    # Call the API with HTTP POST method.
    response = requests.post(
        "https://ollama.com/api/generate", 
        headers={"Authorization": f"Bearer {KEY}"},  # Key is omitted for security purpose
        json=req_payload)
    
    # Get the JSON file
    res_payload = json.loads(response.content)
    
    reply = markdown.markdown(res_payload['response'], output_format = "html")
    return build_table(reply)

# Main Process
def process(prompt: str) -> str:
    try:
        return get_ai_response(prompt)
    except Exception as e:
        return "<p>Cannot connect to the API. Please connect to the Internet and try again.</p>"

def main():
    print()
if __name__ == '__main__':
    main()

