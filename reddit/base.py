import praw
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

reddit = praw.Reddit(user_agent=REDDIT_USER_AGENT,
                  client_id=REDDIT_CLIENT_ID,
                  client_secret=REDDIT_CLIENT_SECRET,
                  username=REDDIT_USERNAME,
                  password=REDDIT_PASSWORD
                  )

