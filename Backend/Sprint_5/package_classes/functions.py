import json

def stringToHtml(filename, string):
    with open('Backend/Sprint_5/Reports/' + filename, "w", encoding="UTF-8") as file:
        file.write(string)

def JSONtoDict(filename):
    with open('Backend/Sprint_5/ejemplos_json/' + filename) as file:
        try:
            return json.load(file)
        except json.decoder.JSONDecodeError:
            print("invalid JSON")