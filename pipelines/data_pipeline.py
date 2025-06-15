import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connect_extract import connect_api, extract_posts
from transform import transform_data, load_csv
from utils.constants import REDDIT_SECRET_KEY, REDDIT_CLIENT, REDDIT_USER_AGENT
import pandas as pd


def pipeline(filename='output.txt', subreddit='dataengineering', time_filter='day', limit=100):
    # reddit instance connection
    instance = connect_api(REDDIT_CLIENT, REDDIT_SECRET_KEY, REDDIT_USER_AGENT)

    posts = extract_posts(instance, subreddit, time_filter, limit)
    posts_data_frame = pd.DataFrame(posts)
    transformed_posts = transform_data(posts_data_frame)

    # loading the dataframe to a csv
    load_csv(transformed_posts, "./data/output.csv")


pipeline()
    