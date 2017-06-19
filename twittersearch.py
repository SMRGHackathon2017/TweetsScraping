from twython import Twython
import sys
import string
import requests
import pandas as pd




# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")

consumer_key = '#####################'
consumer_secret = '######################'
access_token = '#############################'
access_token_secret = '###############################'

twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)

geocode = '51.4543,-0.9781,10mi'


#get twitter search result for string q, 5 tweets, with the search within the geocode radius

user_timeline = twitter.search(q="vacancies",geocode=geocode, count=5)


# unnest the result. just show the text

for tweets in user_timeline["statuses"]:
    print (tweets["text"] + "\n")
