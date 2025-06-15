import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl_pipeline import connect_api, extract_posts
from utils.constants import REDDIT_SECRET_KEY, REDDIT_CLIENT, REDDIT_USER_AGENT

def pipeline(filename='output.txt', subreddit='dataengineering', time_filter='day', limit=100):
    # reddit instance connection
    instance = connect_api(REDDIT_CLIENT, REDDIT_SECRET_KEY, REDDIT_USER_AGENT)

    posts = extract_posts(instance, subreddit, time_filter, limit)

    
pipeline()
    