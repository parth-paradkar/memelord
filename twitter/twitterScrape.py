import datetime
import tweepy
import time
import re
import sys

from twitter.config import (api, twitterAccounts, db)
from imgUpload import uploadImgImgur

cursor = db.cursor()

def addToDB(tweets, tableName):
    newTweets = []

    for tweet in tweets:
        twObj = {}
        twObj['tweet_id'] = tweet['id_str']
        twObj['tweet_screen_name'] = tweet['user']['screen_name']
        if 'text' in tweet:
            text = tweet['text']
        text = re.sub(r"http\S+", "", text).strip()
        twObj['tweet_text'] = text

        twObj['tweet_media_url'] = ""
        try:
            url = tweet['entities']['media'][0]['media_url']
            if url.endswith(".png") or url.endswith(".jpg") or url.endswith(".gif"):
                twObj['tweet_media_url'] = url
                twObj['imgur_url'] = uploadImgImgur(url)
        
        except Exception as e:
            print(e)
        
        ts = tweet['created_at']
        timeStamp = datetime.datetime.strptime(ts, '%a %b %d %H:%M:%S +0000 %Y')

        twObj['tweet_fetched_time'] = int(time.mktime(timeStamp.timetuple()))

        
        placeholders = ', '.join(['%s'] * len(twObj))
        columns = ', '.join(twObj.keys())
        sql = "REPLACE INTO %s  ( %s ) VALUES ( %s )" % (tableName, columns, placeholders)
        cursor.execute(sql, list(twObj.values()))

        newTweets.append(twObj)
    
    return newTweets    

def topTweets(tweets, numberOfTopTweets):
    tweets = sorted(tweets, key = lambda x: x['favorite_count'], reverse = True)
    tweets = tweets[0:numberOfTopTweets]
    addToDB(tweets, "top_tweets")
    return tweets


def scrapeAccount():
    for account in twitterAccounts:
        print("Fetching Tweets for Account: {}".format(account))
        sql = "SELECT `tweet_ID` FROM `fetched_tweets` WHERE `tweet_screen_name` = '{}' ORDER BY `tweet_fetched_time` DESC ".format(account)
    
        cursor.execute(sql)
        try:
            oldest = cursor.fetchall()[0][0]
        except:
            oldest = None

        try:
            tweets = api.user_timeline(screen_name = account, count = 5, since_id = oldest)
            tweetArray = [tweet._json for tweet in tweets]
            addToDB(tweetArray, "fetched_tweets")
            topTweets(tweetArray, 2)
            db.commit()    

        except Exception as e:
            print(e)
