import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input ("did you mean %s instead ? enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]            
        elif yn == "N":
            return "The word doesn't exist. please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. please double check it."
    

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

