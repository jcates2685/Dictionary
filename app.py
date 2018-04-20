import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):

    w = w.lower()

    if w in data:
        return data[w]

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


print(translate(word))
