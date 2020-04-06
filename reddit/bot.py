from setup import reddit
import requests
import json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

post = list(reddit.subreddit('ProgrammerHumor').hot(limit=5))[0].url

headers = {
            'Content-type': 'application/json'
        }

data = {
            'text': post
        }

response = requests.post(os.getenv("SLACK_WEBHOOK"), headers=headers, data=json.dumps(data)) 
