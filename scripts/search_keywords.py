pairings = [
    ["ps5", "stock"],
    ["ps5", "available"],
    ["playstation 5", "available"],
    ["playstation 5", "stock"],
]


def contains_words(pairs, text):
    text_lc = text.lower()
    for a, b in pairs:
        if a.lower() in text_lc and b.lower() in text_lc:
            return True

    return False


def is_in_stock(data_list):
    for data in data_list:
        if contains_words(pairings, data):
            return True
