import json
import time
from helpers import get_post, send_to_slack

with open('subreddits.json', 'r') as f:
    subreddits = json.load(f)['subreddits']
    prev_posts = {}

    if(not prev_posts):
        for sub in subreddits:
            post = get_post(sub)
            prev_posts[sub] = post
            if(post):
                send_to_slack(post)

    while(1):
        for sub in subreddits:
            post = get_post(sub)
            if(post):
                if(post.url != prev_posts[sub].url):
                    print(f'New post on r/{sub}')
                    send_to_slack(post)
                    print(f'Sent post from r/{sub}')
        time.sleep(30)
