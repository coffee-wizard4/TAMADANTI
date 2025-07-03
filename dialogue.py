import json
import random

class Emotion():
    HAPPY = 0
    SAD = 1
    ANGRY = 2

def get_quotes():
    with open("dialogue.json", "r", encoding="utf-8") as f:
        return json.load(f)

quotes = get_quotes()

def get_random_quote(emotion):
    match emotion:
        case Emotion.HAPPY:
            return random.choice(quotes["happy"])
        case Emotion.SAD:
            return random.choice(quotes["sad"])
        case Emotion.ANGRY:
            return random.choice(quotes["angry"])