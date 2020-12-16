import praw
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os
from memelord.config import (
    REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_PASSWORD, REDDIT_USERNAME, REDDIT_USER_AGENT
)

reddit = praw.Reddit(user_agent=REDDIT_USER_AGENT,
                  client_id=REDDIT_CLIENT_ID,
                  client_secret=REDDIT_CLIENT_SECRET,
                  username=REDDIT_USERNAME,
                  password=REDDIT_PASSWORD
                  )

