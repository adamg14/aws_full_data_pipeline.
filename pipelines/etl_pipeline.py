def data_extraction(filename, subreddit, time_filter, limit):
    # reddit instance connection
    instance = connect_reddit(CLIENT_ID, SECRET, "Adam Worede")
    