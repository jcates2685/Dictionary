import json

data = json.load(open("data.json"))


def translate(w):

    w = w.lower()

    if w in data:
        return data[w]
    else:
        return "This word doesn't exist. Please check your spelling."


word = input("Enter word: ")


print(translate(word))

