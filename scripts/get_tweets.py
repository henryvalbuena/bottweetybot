from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DRIVER_PATH = "./geckodriver"


def get_tweets(twitter_user, timeout=5):
    driver = webdriver.Firefox(executable_path=DRIVER_PATH)
    driver.get(twitter_user)
    tweets = []
    try:
        elements = WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "article"))
        )
        for element in elements:
            tweets.append(element.get_attribute("innerText"))
    finally:
        driver.quit()
        print("TWEET LIST")
        print(tweets)
        print("TWEET LIST")
        return tweets
