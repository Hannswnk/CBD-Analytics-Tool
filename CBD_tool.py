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
    return "There are " + str(df.shape[0]) + " tweets in this document."


def top_5_liked():
    # prints the 5 tweets with the highest like count (username, tweet and likes count)
    ndf = df.sort_values("likes_count", ascending=False).head()
    return ndf[["username", "tweet", "likes_count"]]


def most_active_accounts():
    # returns the 5 accounts with the most tweets including the hashtag/key word

    return df.username.value_counts().head()


def top_5_retweeted():
    # prints the 5 tweets with the highest retweet count (username, tweet and likes count)
    nrdf = df.sort_values("retweets_count", ascending=False).head()
    return nrdf[["username", "tweet", "retweets_count"]]


"""def keyword_counter():
    # not yet functional
    keyword_count = {}
    all_words = []

    # cleaning all the tweets from special characters
    clean_tweets_list = []
    clean_tweets_str: str = ""
    for i in df.tweet:
        clean_tweets_list.append(special_character_cleaning(i))
    clean_tweets_str = clean_tweets_str.join(clean_tweets_list)
"""


def special_character_cleaning(str_to_clean):
    # cleans a string from all alphanumerical characters

    working_list = []
    clean_str: str = ""

    for i in str_to_clean:
        if i.isalnum() or i == " ":
            working_list.append(i)
    clean_str = clean_str.join(working_list)
    return clean_str


def export_to_csv():
    with pd.ExcelWriter('output.xlsx') as writer:
        df.to_excel(writer, sheet_name='Tweets')
        final_df.to_excel(writer, sheet_name="Analysis")


def describe_all():
    return df.describe(include="all")


clean_up()
top_5_retweeted_df = top_5_retweeted()
top_5_liked_df = top_5_liked()
most_active_accounts_df = most_active_accounts()
describe_df = describe_all()
tweet_count = tweet_counter()


# print(top_5_retweeted_df, top_5_liked_df, most_active_accounts_df, describe_df, tweet_count)
final_df = pd.concat([top_5_liked_df, top_5_retweeted_df], sort=False, ignore_index=True)
export_to_csv()