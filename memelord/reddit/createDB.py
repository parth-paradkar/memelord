from memelord.db import get_conn
db = get_conn()
cursor = db.cursor()

def create_reddit_table():
    try:
        posts = "CREATE TABLE `reddit_posts` (`ID` INT NOT NULL AUTO_INCREMENT, `post_id` VARCHAR(255) NOT NULL, `post_title` VARCHAR(511) NOT NULL, `subreddit` VARCHAR(255) NOT NULL, `imgur_url` VARCHAR(255), `posted_on_slack` VARCHAR(1) NOT NULL DEFAULT 'N', UNIQUE(`post_id`), PRIMARY KEY(`ID`))"
        cursor.execute(posts)
        db.commit()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    create_reddit_table()