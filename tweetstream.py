#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
import tweepy
import json
import re
#Variables that contain the user credentials to access Twitter API


consumer_key = 'CsZGk92EBPSu6bIdyPm1s8Jfl'
consumer_secret = '4Yk1Elgi7IPpuenvKNLzylIkhWxM8hf8ev7pPTKtbT02iJee9H'
access_token = '3371544088-v2ShB55O460CdG0JbX2ThDjILfFCeT2mXbudzhM'
access_token_secret = '7j7oBVv7YJ16AyGiOjp2tGoFEYzRUIHss3LWAG5JFeFNo'


def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweet_data = json.loads(data)

        if word_in_text("vacanc",tweet_data['text']) or word_in_text("hiring",tweet_data['text']) or word_in_text("staff",tweet_data['text']):

            #print tweet_data['text']
            print (data)
        return True

    def on_error(self, status):
        print (status)



if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()


    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    stream.filter(locations=[-6.42, 49.86, 1.76, 55.81])
   

    #Berkshire = -1.588088,51.328979,-0.490044,51.577825
    
    #England = -6.42,49.86,1.76,55.81
