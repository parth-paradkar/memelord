import os
import json
import requests
from twitter.config import (db, SLACK_WEBHOOK)

def sendMessage():
    cursor = db.cursor()
    sql = "SELECT * FROM top_tweets WHERE posted_on_slack = 'N' ORDER BY RAND()"
    cursor.execute(sql)
    try:
        row = cursor.fetchall()[0]
    except:
        print("No New Tweets :(")
        return False
    
    topTweet = {}
    columns = tuple([d[0] for d in cursor.description] )

    topTweet = dict(zip(columns, row))

    tweet_id = topTweet['tweet_ID']
    media_url = topTweet['tweet_media_url']
    tweet_screen_name= topTweet['tweet_screen_name']
    imgur_url = topTweet['imgur_url']
    tweet_text = topTweet['tweet_text']

    sql = "UPDATE top_tweets SET posted_on_slack = 'Y' WHERE tweet_ID = '{}'".format(tweet_id)
    cursor.execute(sql)
    db.commit()

    print(media_url)
    if not (media_url.endswith(".jpg") or media_url.endswith(".png") or media_url.endswith(".gif")):
        print("Not an Image")
        return False

    headers = {'Content-Type': 'application/json'}

    if tweet_text is '':
        postText = "{}".format(imgur_url)
    else:
        postText = "{}\n{}".format(tweet_text, imgur_url)

    data = {
        "text" : postText, 
        "attachments": [{
            "text": "Via @{}".format(tweet_screen_name)
        }]
    }

    data = json.dumps(data)
    print(data)
    
    r = requests.post(SLACK_WEBHOOK, data=data, headers=headers)
    if r.status_code == 200:
        print(str(r.status_code) +" OK")
        print("Successfully Posted to Slack")

    else:
        print("Failed: {}".format(r.status_code))
    
    return topTweet 
