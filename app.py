import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):

    w = w.lower()

    if w in data:
        print(w)
        return data[w]
    elif w.title() in data:
        print(w.title())
        return data[w.title()]
    elif w.upper() in data:
        print(w.upper())
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        confirm = input("Did you mean to type %s? Enter Y or N" % get_close_matches(w, data.keys())[0])

        if confirm == "Y" or confirm == "y":
            return data[get_close_matches(w, data.keys())[0]]

        elif confirm == "N" or confirm == "n":
            return "This word doesn't exist. Please check your spelling."

        else:
            return "We didn't understand your input"

    else:
        return "This word doesn't exist. Please check your spelling."


word = input("Enter word: ")

output = translate(word)
count = 0

if type(output) == list:
    for item in output:
        count += 1
        print(str(count) + ". " + item)
else:
    print(output)
