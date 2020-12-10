# Replace the values in the fields below with your own info

[DATABASE]
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")
database = os.getenv("MYSQL_DATABASE")

[TWITTER]
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET_KEY")

[BOT]
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

[IMAGEUPLOAD]
client_id = os.getenv("IMGUR_CLIENT_ID")
imgur_upload_url = "https://api.imgur.com/3/image"

[REDDIT]
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USERNAME = os.getenv("REDDIT_USERNAME")
REDDIT_PASSWORD = os.getenv("REDDIT_PASSWORD")
