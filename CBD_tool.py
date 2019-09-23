import pandas as pd
from collections import Counter

# importing the CSV
df = pd.read_csv("TwintCBDWorkfile.csv")

# creating empty data frames to merge after they have been filled
final_df: DataFrame = pd.DataFrame(columns=['X', 'Y', 'Z'])
top_5_liked_df: DataFrame = pd.DataFrame(columns=['X', 'Y', 'Z'])
top_5_retweeted_df: DataFrame = pd.DataFrame(columns=['X', 'Y', 'Z'])
most_active_accounts_df: DataFrame = pd.DataFrame(columns=['X', 'Y', 'Z'])


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
    top_5_liked_df = ndf[["username", "tweet", "likes_count"]]


def most_active_accounts():
    # returns the 5 accounts with the most tweets including the hashtag/key word
    print("The following accounts have tweeted the most about the topic:")
    most_active_accounts_df = df.username.value_counts().head()


def top_5_retweeted():
    # prints the 5 tweets with the highest retweet count (username, tweet and likes count)
    nrdf = df.sort_values("retweets_count", ascending=False).head()
    top_5_retweeted_df = nrdf[["username", "tweet", "retweets_count"]]
    print(top_5_retweeted_df)


def special_character_cleaning(str_to_clean):
    # cleans a string from all alphanumerical characters

    working_list = []
    clean_str: str = ""

    for i in str_to_clean:
        if i.isalnum() or i == " ":
            working_list.append(i)
    clean_str = clean_str.join(working_list)
    return clean_str


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


def export_to_csv():
    with pd.ExcelWriter('output.xlsx') as writer:
        df.to_excel(writer, sheet_name='Tweets')
        final_df.to_excel(writer, sheet_name="Analysis")


def describe():
    describe_df = df.describe(include="all")


def run_all():
    clean_up()
    tweet_counter()
    top_5_liked()
    top_5_retweeted()
    most_active_accounts()
    describe()
    export_to_csv()


run_all()
