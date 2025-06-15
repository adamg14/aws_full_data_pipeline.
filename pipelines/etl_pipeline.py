from praw import Reddit 


def connect_api(client_id, client_secret, user_agent):
    try:
        reddit = Reddit(
            client_id,
            client_secret,
            user_agent
        )
        print("connected to reddit!")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)


def extract_posts(instance, subreddit, limit):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter, )