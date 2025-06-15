from praw import Reddit
import sys

def connect_api(client_id, client_secret, user_agent):
    try:
        reddit = Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        print("connected to reddit!")
        return reddit
    except Exception as e:
        print(f"Error connecting to Reddit: {e}")
        sys.exit(1)


def extract_posts(reddit_instance, subreddit_name, time_filter, limit):
    try:
        subreddit = reddit_instance.subreddit(subreddit_name)
        posts = []
        
        for post in subreddit.top(time_filter=time_filter, limit=limit):
            posts.append({
                "title": post.title,
                "score": post.score,
                "url": post.url,
                "id": post.id,
                "num_comments": post.num_comments
            })
        
        print(posts)
        return posts

    except Exception as e:
        print(f"Error extracting posts: {e}")
        return []