import schedule
import tweepy,requests,os,time
from constants import *
    # CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from Quotes_text import *
def jobmain():
    consumer_key=CONSUMER_KEY
    consumer_secret=CONSUMER_SECRET
    access_token=ACCESS_TOKEN
    access_token_secret=ACCESS_TOKEN_SECRET


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    auth.secure= True

    api = tweepy.API(auth)
    def tweet_quote(quote):

        api = tweepy.API(auth)

        api.update_status("{} #quotesquota  #qotd  #dailyquotes".format(quote))
        print("Status updated to twitter")

    while True:
        Quote=Quotes_list[0]
        tweet_quote(Quotes_list[0])
        return_val = Quotes_list.pop(0)
        print(return_val)
        print(Quotes_list[0])
        break

    time.sleep(3600)


schedule.every(1).minutes.do(jobmain)

while True:
    schedule.run_pending()
    time.sleep(1)