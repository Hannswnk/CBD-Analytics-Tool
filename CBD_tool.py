import pandas as pd
import xlsxwriter
import subprocess
from collections import Counter

# importing the CSV
df = pd.read_csv("tweets.csv")

# getting time stamps to be displayed on top of document
date_created = df["date"][0]
time_created = df["time"][0]



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
    return df.username.value_counts().head().rename_axis('Username').reset_index(name='Number of Tweets')


def top_5_retweeted():
    # prints the 5 tweets with the highest retweet count (username, tweet and likes count)
    nrdf = df.sort_values("retweets_count", ascending=False).head()
    return nrdf[["username", "tweet", "retweets_count"]]


def keyword_counter():
    # not yet functional
    keyword_count = {}
    all_words = []

    # cleaning all the tweets from special characters
    clean_tweets_list = []
    clean_tweets_str: str = ""
    for i in df.tweet:
        clean_tweets_list.append(special_character_cleaning(i))
    clean_tweets_str = clean_tweets_str.join(clean_tweets_list)


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
    # setting the name
    writer = pd.ExcelWriter("extra_output.xlsx", engine='xlsxwriter')

    # actual data to be added
    top_5_retweeted().to_excel(writer, sheet_name='Analysis', startcol=1, startrow=8, index=False)
    top_5_liked().to_excel(writer, sheet_name='Analysis', startcol=1, startrow=17, index=False)
    most_active_accounts().to_excel(writer, sheet_name='Analysis', startcol=1, startrow=26, index=False)

    # some more declarations - don't touch
    workbook = writer.book
    worksheet = writer.sheets["Analysis"]

    # adds a sheet with all tweets
    df.to_excel(writer, sheet_name='Tweets')
    worksheet2 = writer.sheets["Tweets"]

    # declaring formats
    bold = workbook.add_format({'bold': True})
    caption = workbook.add_format({'bold': True, 'font_size': '16'})
    box = workbook.add_format({'border': 1, "border_color": "#000000"})

    # adding captions
    worksheet.write('B2', "Date created:", bold)
    worksheet.write('B3', "Time created:", bold)
    worksheet.write('C2', date_created)
    worksheet.write('C3', time_created)
    worksheet.write('B5', "Tweet Counter:", bold)
    worksheet.write('C5', tweet_counter())
    worksheet.write('B7', 'Top 5 Retweeted', caption)
    worksheet.write('B16', 'Top 5 Liked', caption)
    worksheet.write('B25', 'Users with the most tweets', caption)
    worksheet.conditional_format('B9:D14', {'type': 'no_blanks', 'format': box})
    worksheet.conditional_format('B27:D32', {'type': 'no_blanks', 'format': box})
    worksheet.conditional_format('B18:D23', {'type': 'no_blanks', 'format': box})

    # formatting rows and coloumns
    worksheet.set_column(0, 0, 5)  # Column  A   width set to 5.
    worksheet.set_column(1, 1, 30)
    worksheet.set_column(2, 2, 60)
    worksheet.set_column(3, 3, 15)

    # closing the workbook
    workbook.close()


clean_up()
export_to_csv()

# opens the file automatically
subprocess.call([r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE', r"C:\Users\hanns\Desktop\CBD\CBD-Analytics-Tool\extra_output.xlsx"])