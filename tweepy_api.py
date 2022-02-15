import tweepy

consumer_key = "RrWfxBBnXDOxlZNqYirfDX5Xj"
consumer_secret = "t15QQotdHZ7TVYfDkmrARiSGnR3PgYzenbwQoEAnKWTQFeySEk"
access_token = "1396401069488435201-vu0VkpiRKx4mnv4c1Vqp3yFNSzZVL4"
access_secret = "attkF6OU35Ms3ounBOiPKdof38T1tqYAbP8GE3906Vnrd"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

topic = "#ipl2022"
date_since = "2022-02-14"

tweets = tweepy.Cursor(api.search_tweets, q=topic, since=date_since).items(20)

for tw in tweets:print(tw.text)










