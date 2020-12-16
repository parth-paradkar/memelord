from memelord.reddit.helpers import get_posts, insert_db
from memelord.config import REDDIT_SUBREDDITS, REDDIT_FETCH_LIMIT

if __name__ == "__main__":
    for sub in REDDIT_SUBREDDITS:
        for post in get_posts(sub, REDDIT_FETCH_LIMIT):
            insert_db(post)