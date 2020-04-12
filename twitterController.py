import time
from twitter.twitterScrape import scrapeAccount
from twitter.slackUpload import sendMessage

try:
    scrapeAccount()
except Exception as e:
    print(e)

print("Sleeping for 30 seconds")
time.sleep(30)

try:
    sendMessage()
except Exception as e:
    print(e)
