# -*- coding: utf-8 -*-
"""
Created on Thu May 14 13:15:02 2020

@author: Personal
"""
import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 

class TwitterClient(object): 
    ''' 
    Generic Twitter Class for sentiment analysis. 
    '''
    def __init__(self): 
        ''' 
        Class constructor or initialization method. 
        '''
        # keys and tokens from the Twitter Dev Console 
        consumer_key = "Zm3yk6NO21n6bSqLk9cRz5VHM"
        consumer_secret = "0k5kfFqNGgmhuAXgqYDhFSW6czoASfQchIzassTisgD0Ixx0py"
        access_token = "1235855507325239297-0qrIDAvSWJApyCIhtlUfA3AUOq1xQR"
        access_token_secret = "qxyoQnxyVoxkZPFQpxKteT3UW6XzhyxlCyXUKL1jrzryb"

        # attempt authentication 
        try: 
            # create OAuthHandler object 
            self.auth = OAuthHandler(consumer_key, consumer_secret) 
            # set access token and secret 
            self.auth.set_access_token(access_token, access_token_secret) 
            # create tweepy API object to fetch tweets 
            self.api = tweepy.API(self.auth) 
        except: 
            print("Error: Authentication Failed") 

    def clean_tweet(self, tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())  

    def get_tweet_sentiment(self, tweet): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(self.clean_tweet(tweet)) 
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'

    def get_tweets(self, query, count = 10): 
        ''' 
        Main function to fetch tweets and parse them. 
        '''
        # empty list to store parsed tweets 
        tweets = [] 

        try: 
            # call twitter api to fetch tweets 
            fetched_tweets = self.api.search(q = query, count = count) 

            # parsing tweets one by one 
            for tweet in fetched_tweets: 
                # empty dictionary to store required params of a tweet 
                parsed_tweet = {} 

                # saving text of tweet 
                parsed_tweet['text'] = tweet.text 
                # saving sentiment of tweet 
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) 

                # appending parsed tweet to tweets list 
                if tweet.retweet_count > 0: 
                    # if tweet has retweets, ensure that it is appended only once 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 

            # return parsed tweets 
            return tweets 

        except tweepy.TweepError as e: 
            # print error (if any) 
            print("Error : " + str(e)) 

def main(): 
    # creating object of TwitterClient Class 
    api = TwitterClient() 
    # calling function to get tweets 
    tweets = api.get_tweets(query = input('enter the query item: '), count = 1000) 

    # picking positive tweets from tweets 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] 
    # percentage of positive tweets 
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
    # picking negative tweets from tweets 
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    # percentage of negative tweets 
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) 
    # percentage of neutral tweets 
    #print("Neutral tweets percentage: {} %".format(100*len(tweets - ntweets - ptweets)/len(tweets))) 

    # printing first 5 positive tweets 
    """
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:30]: 
        print(tweet['text']) 
    """  
    
    positive=(100*len(ptweets)/len(tweets))
    negative=(100*len(ntweets)/len(tweets))
    
    if negative==0:
        ratingbase=positive+20
    else:
        ratingbase=positive-negative
    
    
    if ratingbase<0:
        ratingbase=(-1)*ratingbase
    elif ratingbase==0:
        ratingbase=12.5
    else:
        ratingbase=ratingbase
    rating=(ratingbase/50)*100
    #print(rating)
    if rating>0 and rating<20:
        print('** - 2 star')
    elif rating>20 and rating<40:
        print("**' - 2.5 star")
    elif rating>40 and rating<60:
        print('*** - 3 star')
    elif rating>60 and rating<80:
        print('**** - 4 star')
    else:
        print('***** - 5 star')
    
     
    # printing first 5 negative tweets 
    #print("\n\nNegative tweets:") 
    #for tweet in ntweets[:10]: 
        #print(tweet['text'])
        
if __name__ == "__main__": 
    # calling main function 
    main() 