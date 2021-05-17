from scripts.get_tweets import get_tweets
from scripts.search_keywords import is_in_stock
from scripts.send_discord_alert import send_alert


users = [
    "https://twitter.com/EBGamesCanada",
    "https://twitter.com/BBYC_Gamers",
    "https://twitter.com/WalmartCAGaming",
]

for user in users:
    tweets = get_tweets(user)
    if is_in_stock(tweets):
        msg = f"{user} has PS5 consoles in stock!!!"
        print(msg)
        send_alert(msg)

print("End of script...")
