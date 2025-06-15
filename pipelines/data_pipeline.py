from etl_pipeline import connect_api

def pipeline(filename, subreddit, time_filter, limit):
    # reddit instance connection
    instance = connect_api(CLIENT_ID, SECRET, "14adam")

    posts = extract_posts(instance, subreddit, time_filter, limit)

    


    