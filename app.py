from scripts.get_tweets import get_tweets
from scripts.search_keywords import is_in_stock


users = ["https://twitter.com/EBGamesCanada", "https://twitter.com/BBYC_Gamers"]

for user in users:
    tweets = get_tweets(user)
    if is_in_stock(tweets):
        print(f"{user} has PS5 consoles in stock!!!")

print("End of script...")