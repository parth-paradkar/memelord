from os import getenv
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

SLACK_WEBHOOK = getenv("SLACK_WEBHOOK")
IMGUR_CLIENT_ID = getenv("IMGUR_CLIENT_ID")

MYSQL_USER = getenv("MYSQL_USER")
MYSQL_PASSWORD = getenv("MYSQL_PASSWORD")
MYSQL_HOST = getenv("MYSQL_HOST")
MYSQL_DATABASE = getenv("MYSQL_DATABASE")

REDDIT_USER_AGENT = getenv("REDDIT_USER_AGENT")
REDDIT_CLIENT_ID = getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = getenv("REDDIT_PASSWORD")
REDDIT_FETCH_LIMIT = 5
REDDIT_SUBREDDITS = [
    "ProgrammerHumor", "softwaregore"
]