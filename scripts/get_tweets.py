import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = "./geckodriver"
RE_1 = "(\\n\d+)*$"
RE_2 = "@\w+\\n"
RE_3 = "\\n[\w ]+\\n"


def extract_tweet(tweet):
    a = re.split(RE_1, tweet)[0]
    b = re.split(RE_2, a, maxsplit=1)[1]

    return re.split(RE_3, b)[1]


def get_tweets(twitter_user, timeout=5):
    driver = webdriver.Firefox(executable_path=DRIVER_PATH)
    driver.get(twitter_user)
    tweets = []
    try:
        elements = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "article"))
        )
        for element in elements:
            clean_tweet = extract_tweet(element.get_attribute("innerText"))
            tweets.append(clean_tweet)
    finally:
        driver.quit()
        print("TWEET LIST")
        print(tweets)
        print("TWEET LIST")
        return tweets
