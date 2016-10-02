#!/usr/bin/python
import twitter, sys, getpass, os

def call_api(username,password):
    consumer_key=''
    consumer_secret=''
    access_token_key=''
    access_token_secret=''
    api = twitter.Api(username, password, access_token_key,access_token_secret)
    friends = api.GetFriends()
    followers = api.GetFollowers()
    heathens = filter(lambda x: x not in followers,friends)
    print "There are %i people you follow who do not follow you:" % len(heathens)
    for heathen in heathens:
        print heathen.screen_name

if __name__ == "__main__":
    password = getpass.getpass()
    call_api(sys.argv[1], password)
