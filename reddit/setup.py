import praw
import json
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os


reddit = praw.Reddit(user_agent=os.getenv("REDDIT_USER_AGENT"),
                  client_id=os.getenv("REDDIT_CLIENT_ID"),
                  client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
                  username=os.getenv("REDDIT_USERNAME"),
                  password=os.getenv("REDDIT_PASSWORD")
                  )

