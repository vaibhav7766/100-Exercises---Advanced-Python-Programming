from collections import ChainMap


english_scoreboard = {
    " ": 0,
    "eaionrtlsu": 1,
    "dg": 2,
    "bcmp": 3,
    "fhwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10,
}


def score(word):
    scores = ChainMap(
        *[dict.fromkeys(letter, score) for letter, score in english_scoreboard.items()]
    )
    return sum([scores[letter] for letter in word])
