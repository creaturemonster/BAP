import pandas as pd
import pip
pip.main(["install","twitter"])
import json
import twitter
from twitter import Twitter
from twitter import OAuth
from twitter import TwitterHTTPError
from twitter import TwitterStream
ck="4utyWgvDx6HziBbOOMrk9A8Zx"
cksecret="bOulyl2Uac0hGayZSDwrZm1o2ULkTZMLUYubOmEXSkwjPhYVJy"
ACCESS_Token="824423500991660032-6mBuL78cft4sIPx0dnEYrKiDNjIXZz1"
ACCESS_Secret="fvg7ptaTu9cD5OqAYjCE4cIn3REDjOy6Fv8TP24aHCguD"
oauth = OAuth(ACCESS_Token, ACCESS_Secret, ck, cksecret)
oauth = OAuth(ACCESS_Token,ACCESS_Secret,ck,cksecret)
twit_api = Twitter(auth=oauth)
twit_api = Twitter(auth=oauth)
oauth = OAuth(ACCESS_Token,ACCESS_Secret,ck,cksecret)
twit_api = Twitter(auth=oauth)
twitter = Twitter(auth=oauth)
twitter.search.tweets(q='#trump')
twitter.search.tweets(q='#trump', result_type='recent', lang='en', count=10)
statuses[0]
{'contributors': None,
 'coordinates': None,
 'created_at': 'Tue Feb 07 22:41:13 +0000 2017',
 'entities': {'hashtags': [{'indices': [9, 23], 'text': 'BrexitBritain'},
   {'indices': [47, 53], 'text': 'trump'},
   {'indices': [55, 63], 'text': 'Erdogan'},
   {'indices': [68, 78], 'text': 'Netanyahu'},
   {'indices': [94, 97], 'text': 'EU'}],
  'symbols': [],
  'urls': [],
  'user_mentions': []},
 'favorite_count': 0,
 'favorited': False,
 'geo': None,
 'id': 829097712280797190,
 'id_str': '829097712280797190',
 'in_reply_to_screen_name': None,
 'in_reply_to_status_id': None,
 'in_reply_to_status_id_str': None,
 'in_reply_to_user_id': None,
 'in_reply_to_user_id_str': None,
 'is_quote_status': False,
world_trends = twitter.trends.available(_woeid=1)
df3=json_normalize(world_trends)
print(df3)
df3.columns
print(df3[df3.name=='New York'])
print(df3[df3.name=='Nashville'])
NYC_id=2459115
Nash_id=2457170  
NYC_trends=twit_api.trends.place(_id=2459115)
from pandas.io.json import json_normalize
df4=json_normalize(NYC_trends,'trends')
df4.ix[0]
Nash_trends=twit_api.trends.place(_id=2457170)
df5=json_normalize(Nash_trends,'trends')
df5.ix[0]
for label, df4[0:20] in ("trends", NYC_trends):
    c=Counter(data)
    plt.hist(c.values())
    plt.title("NYC Trends")
    plt.ylabel("The Frequency of the Trends")
    plt.xlabel("The trends")
    plt.figure()
for label, df5[0:20] in ("trends", Nash_trends):
    c=Counter(data)
    plt.hist(c.values())
    plt.title("Nash Trends")
    plt.ylabel("The Frequency of the Trends")
    plt.xlabel("The trends")
    plt.figure()
df4[['name','tweet_volume']].plot(kind='bar')
df5[['name','tweet_volume']].plot(kind='bar')



