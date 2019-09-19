import pandas as pd
from collections import Counter


# importing the CSV
df = pd.read_csv("TwintCBDWorkfile.csv")


def clean_up():
    # drops all the unnecessary columns
    df.drop(["id", "conversation_id", "created_at", "user_id", "quote_url", "place", "mentions", "urls", "photos",
             "cashtags", "video", "user_rt_id", "near", "geo"], axis=1, inplace=True)


def tweet_counter():
    # returns the number of tweets in the document
    print("There are " + str(df.shape[0]) + " tweets in this document.")


def top_5_liked():
    # prints the 5 tweets with the highest like count (username, tweet and likes count)
    ndf = df.sort_values("likes_count", ascending=False).head()
    print(ndf[["username", "tweet", "likes_count"]])


def most_active_accounts():
    # returns the 5 accounts with the most tweets including the hashtag/key word
    print("The following accounts have tweeted the most about the topic:")
    print(df.username.value_counts().head())


def top_5_retweeted():
    # prints the 5 tweets with the highest retweet count (username, tweet and likes count)
    nrdf = df.sort_values("retweets_count", ascending=False).head()
    print(nrdf[["username", "tweet", "retweets_count"]])


def keyword_counter():
    keyword_count = {}
    for i in df.tweet:
        str(df.tweet[i]).split(" ")



def run_all():
    clean_up()
    tweet_counter()
    top_5_liked()
    top_5_retweeted()
    most_active_accounts()


keyword_counter()
