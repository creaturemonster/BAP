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
q='#trump'
count=2100
search_results=twit_api.search.tweets(q=q,count=count)
statuses=search_results['statuses']
statuses[0]['text']
status_texts=[status['text'] for status in statuses]
screen_names=[user_mention['screen_name']
    for status in statuses
        for user_mention in status['entities']['user_mentions']]
hashtags=[hashtag['text']
    for status in statuses 
        for hashtag in status['entities']['hashtags']]
words = [ w
    for t in status_texts
        for w in t.split()]
print(json.dumps(status_texts[0:5],indent=1))
print(json.dumps(screen_names[0:5],indent=1))
print(json.dumps(hashtags[0:5],indent=1))
print(json.dumps(words[0:5],indent=1))
from collections import Counter
for item in [words,screen_names, hashtags]:
        c=Counter(item)
        print(c.most_common()[:10])
        print()
import pip
pip.main(["install","prettytable"])
from prettytable import PrettyTable
for label, data in (("Word",words),('Screen Name',screen_names),('Hashtag',hashtags)):
    pt=PrettyTable(field_names=[label,'Count'])
    c=Counter(data)
    [pt.add_row(kv) for kv in c.most_common()[:10]]
    pt.align[label],pt.align["Count"]="l","r"
    print(pt)
retweets=[
    (status['retweet_count'],
    status['retweeted_status']['user']['screen name'],
    status['text'])
    for status in statuses
        if status.has_key['retweeted_status']]
_retweets=twitter_api.statuses.retweets(id=317127304981667841)
print(r['user']['screen_name'] for r in _retweets)
from matplotlib import pyplot as plt
word_counts=sorted(Counter(words).values(),reverse=True)
plt.loglog(word_counts)
plt.ylabel("Freq")
plt.xlabel("Word Rank")
for label, data in (('Words',words),('Screen Names', screen_names),("Hashtags",hashtags)):
        c=Counter(data)
        plt.hist(list(c.values()))
        plt.title(label)
        plt.ylab("Number of Items in Bin")
        plt.xlab("Bins(Number of times an item appeared)")
        plt.figure()
counts=[count for count, _,_ in retweets]
plt.hist(counts)
plt.title("Retweets")
plt.xlabel('Bins (number of times retweeted)')
plt.ylabel('Number of tweets in the Bin')
print(counts)






















