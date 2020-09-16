import pip
pip.main(["install","twitter"])
import json
from twitter import Twitter 
from twitter import OAuth 
from twitter import TwitterHTTPError 
from twitter import TwitterStream 
ck="4utyWgvDx6HziBbOOMrk9A8Zx"
cksecret="bOulyl2Uac0hGayZSDwrZm1o2ULkTZMLUYubOmEXSkwjPhYVJy"
ACCESS_Token="824423500991660032-6mBuL78cft4sIPx0dnEYrKiDNjIXZz1"
ACCESS_Secret="fvg7ptaTu9cD5OqAYjCE4cIn3REDjOy6Fv8TP24aHCguD"
oauth = OAuth(ACCESS_Token, ACCESS_Secret, ck, cksecret)
twitter = Twitter(auth=oauth)
twitter.search.tweets(q='#rutgers')
twitter.search.tweets(q='#rutgers', result_type='recent', lang='en', count=10)
world_trends = twitter.trends.available(_woeid=1)
sa_trends = twitter.trends.place(_id = 56120136)
sfo_trends = twitter.trends.place(_id = 2487956)
print(json.dumps(sa_trends, indent=4))
newyork_trends = twitter.trends.place(_id = 2459115)
newyork_trends = twitter.trends.place(_id = 2487956)
print(json.dumps(newyork_trends, indent=4))
spain_trends = twitter.trends.place(_id = 23424950)
spain_trends = twitter.trends.place(_id = 23424950)
print(json.dumps(spain_trends, indent=4))
italy_trends = twitter.trends.place(_id = 2459115)
italy_trends = twitter.trends.place(_id = 2487956)
print(json.dumps(italy_trends, indent=4))
saudi_trends = twitter.trends.place(_id = 56120136)
saudi_trends = twitter.trends.place(_id = 56120136)
print(json.dumps(saudi_trends, indent=4))
twitter.followers.ids(screen_name="FeliciaMcGinty")
twitter.statuses.user_timeline(screen_name="FeliciaMcGinty")
twitter.followers.ids(screen_name="")
twitter.statuses.user_timeline(screen_name="")


