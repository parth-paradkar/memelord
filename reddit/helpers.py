from base import reddit, SLACK_WEBHOOK
import config

headers = { 'Content-type': 'application/json' }

def get_post(subreddit):
    post = list(reddit.subreddit(subreddit).hot(limit=1))[0]
    if(post.url.endswith('.png') or post.url.endswith('.jpg')):
        return post
    return None

def _format_post(post):
        return { 'text': f'r/{post.subreddit.display_name} {post.title}\n{post.url}' }

def send_to_slack(data):
    return requests.post(SLACK_WEBHOOK, 
            headers=headers, 
            data=json.dumps(_format_post(data))
            )
