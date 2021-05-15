import re

pairings = {
    "pair1": ["ps5", "stock"],
    "pair2": ["ps5", "available"],
    "pair3": ["playstation", "available"],
    "pair4": ["playstation", "stock"],
}


def contains_words(text):
    return (
        (
            re.search(pairings["pair1"][0], text, re.I)
            and re.search(pairings["pair1"][1], text, re.I)
        )
        or (
            re.search(pairings["pair2"][0], text, re.I)
            and re.search(pairings["pair2"][1], text, re.I)
        )
        or (
            re.search(pairings["pair3"][0], text, re.I)
            and re.search(pairings["pair3"][1], text, re.I)
        )
        or (
            re.search(pairings["pair4"][0], text, re.I)
            and re.search(pairings["pair4"][1], text, re.I)
        )
    )


def is_in_stock(data_list):
    for data in data_list:
        if contains_words(data):
            return True
