from memelord.reddit.helpers import send_to_slack
from memelord.db import get_conn

def post_to_slack():
    db = get_conn()
    cursor = db.cursor()
    select_statement = "SELECT * FROM reddit_posts WHERE posted_on_slack != 'Y' ORDER BY ID DESC LIMIT 1"
    cursor.execute(select_statement)
    cols = [e[0] for e in cursor.description]
    post = dict(zip(cols, list(cursor)[0]))
    data = {
        'text': f"Via r/{post['subreddit']} - {post['post_title']}\n{post['imgur_url']}"
    }
    response = send_to_slack(data)
    if(response.ok):
        update_query = f"UPDATE reddit_posts SET posted_on_slack = 'Y' WHERE post_id = '{post['post_id']}'"
        cursor.execute(update_query)
        db.commit()
    cursor.close()
    db.close()


post_to_slack()