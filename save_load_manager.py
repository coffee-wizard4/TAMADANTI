import json

def load():
    with open("data.json", "r", encoding= "utf-8") as f:
        return json.load(f)

def save(hunger, attention):
    newobj = {
        "hunger" : hunger,
        "attention" : attention
    }
    with open("data.json", "w", encoding= "utf-8") as f:
        json.dump(newobj, f)