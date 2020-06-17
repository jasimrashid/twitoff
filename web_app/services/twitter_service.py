import os 
import tweepy
from dotenv import load_dotenv
from tweepy import OAuthHandler, API

load_dotenv

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

api = API(auth)
print("API CLIENT", api)

if __name__ == "__main__":
    user = api.get_user("realDonaldTrump")
    print("TWITTER USER:", type(user))

    print(user.id)
    print(user.screen_name)
    print(user.name)


    tweets = api.user_timeline("realDonaldTrump", tweet_mode = "extended")
    print("TWEETS", type(tweets))
    print(type(tweets[0]))


    tweet = tweets[0]
    print(tweet.id)
    print(tweet.full_text)
    # breakpoint()















