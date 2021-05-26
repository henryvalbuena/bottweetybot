from persistence.check_db import db_init
from persistence.model import Tweet

session = db_init()

pairings = [
    ["ps5", "stock"],
    ["ps5", "available"],
    ["playstation 5", "available"],
    ["playstation 5", "stock"],
]


def contains_words(pairs, text):
    text_lc = text.lower()
    for a, b in pairs:
        if a.lower() in text_lc and b.lower() in text_lc and not is_repeated(text_lc):
            return True

    return False


def is_repeated(msg):
    query = session.query(Tweet)
    filter_ = query.filter(Tweet.msg == msg).all()

    if len(filter_) > 0:
        return True
    else:
        new_msg = Tweet(msg=msg)
        session.add(new_msg)
        session.commit()

        return False


def is_in_stock(data_list):
    for data in data_list:
        if contains_words(pairings, data):
            return True
