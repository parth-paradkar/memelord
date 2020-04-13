import json
import os
import tweepy
import mysql.connector as mysql

from dotenv import (load_dotenv, find_dotenv)

load_dotenv(find_dotenv())

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
database = os.getenv("MYSQL_DATABASE")


consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET_KEY")

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

db = mysql.connect(user=user, passwd=password, host=host, database=database)

with open("twitter/twitter-accounts.json") as f:
    data = json.load(f)
    twitterAccounts = data['twitterAccounts']

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

