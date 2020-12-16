from memelord.reddit.base import reddit
import requests
import json
from memelord.config import SLACK_WEBHOOK, REDDIT_SUBREDDITS
from memelord.imgUpload import uploadImgImgur
from memelord.db import get_conn

headers = { 'Content-type': 'application/json' }

def get_posts(subreddit, limit):
    posts = list(reddit.subreddit(subreddit).hot(limit=limit))
    for post in posts:
        if(post.url.endswith('.png') or post.url.endswith('.jpg')):
            yield post

def _format_post(post_data):
        return { 'text': f'Via r/{post.subreddit.display_name}: {post.title}\n{post.url}' }

def send_to_slack(data):
    return requests.post(SLACK_WEBHOOK, 
            headers=headers, 
            data=json.dumps(data)
            )

def insert_db(post):
    try:
        db = get_conn()
        cursor = db.cursor()
        existing_post_statement = f"SELECT * FROM reddit_posts WHERE post_id = '{post.id}'" 
        cursor.execute(existing_post_statement)
        existing_post = list(cursor)
        if(not existing_post):
            imgur_url = uploadImgImgur(post.url)
            statement = f"INSERT INTO reddit_posts ( post_id, subreddit, post_title, imgur_url ) VALUES ( '{post.id}', '{post.subreddit.display_name}', '{post.title}', '{imgur_url}' )"
            cursor.execute(statement)
            db.commit()
            cursor.close()
    except Exception as e:
        print(e)
    finally:
        db.close()
