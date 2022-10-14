from distutils.command.config import config
from os import access
import tweepy
import configparser
import pandas as pd

config= configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret= config['twitter']['api_key_secret']

access_token= config['twitter']['access_token']
access_token_secret= config['twitter']['access_token_secret']

auth= tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api= tweepy.API(auth)

client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAKi2iAEAAAAAdryPVdwrr5ia%2F8YesXmRnIKLPHI%3DD0sNR9YIR0u8N6WxiOSi9YuCrD5vucNaLNZNV1QLUKF8VTCZLM')

query = '#emociones -is:retweet lang:es'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)


for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)


df= pd.DataFrame(tweets)

df.to_csv('tweets.csv')








