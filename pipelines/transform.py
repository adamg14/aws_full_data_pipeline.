import pandas as pd


def transform_data(posts):
    posts['created_utc'] = pd.to_datetime(posts['created_utc'], unit='s')
    posts['author'] = posts['author'].astype(str)

    return posts


def load_csv(posts, path):
    posts.to_csv(path, index=False)
