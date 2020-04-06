from setup import reddit
import requests
import json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

headers = { 'Content-type': 'application/json' }

with open('subreddits.json', 'r') as f:
    data = json.load(f)
    subreddits = data['subreddits']
    for sub in subreddits:
        post = list(reddit.subreddit(sub).hot(limit=5))[0]
        if(post.url.endswith('.png') or post.url.endswith('.jpg')):
            data = { 'text': f'r/{sub} {post.title}\n{post.url}' }
            response = requests.post(os.getenv("SLACK_WEBHOOK"), headers=headers, data=json.dumps(data))
