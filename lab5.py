lecture_5_problem_1.py
Long ago
Apr 22, 2018

You uploaded an item
Text
lecture_5_problem_1.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import pip
pip.main(["install","twitter"])
pip.main(["install","textblob"])
from textblob import TextBlob

import twitter
from twitter import Twitter
from twitter import OAuth
from twitter import TwitterHTTPError
from twitter import TwitterStream
from pandas.io.json import json_normalize

from textblob import TextBlob



ck = "gwEdUQjvo9JDSLMpii205Q06O"
cs = "OlA4PIlLfpZ5HcEAGPOIJx4DwduhmACShoGQ66mJYt4ocxShwX"
at = "823996990329589760-1wW34frljiy7HrWp777qGFzOhEZksMW"
ats = "nzbKJCBUqlCsP6MNe5CFrOzZHo4wcvbubt1nJTqRkvFiB"

oauth = OAuth(at,ats,ck,cs)
api = Twitter(auth=oauth)

q1 = 'Trump'
q2 = 'Hillary'
q3 = 'BernieSanders'

search_results = api.search.tweets(q=q1,count = 100)
df1 = json_normalize(search_results, 'statuses')
search_results = api.search.tweets(q=q2,count = 100)
df2 = json_normalize(search_results, 'statuses')
search_results = api.search.tweets(q=q3,count = 100)
df3 = json_normalize(search_results, 'statuses')

s = np.empty(0)
p = np.empty(0)

for x in df1['text']:
    w = TextBlob(x)
    w.sentiment
    s=np.append(s,w.subjectivity)
    #print(w.subjectivity)
    p=np.append(p,w.polarity)
    
s2 = np.empty(0)
p2 = np.empty(0)

for x in df2['text']:
    w = TextBlob(x)
    w.sentiment
    s2=np.append(s2,w.subjectivity)
    #print(w.subjectivity)
    p2=np.append(p2,w.polarity)
    
s3 = np.empty(0)
p3 = np.empty(0)

for x in df3['text']:
    w = TextBlob(x)
    w.sentiment
    s3=np.append(s3,w.subjectivity)
    #print(w.subjectivity)
    p3=np.append(p3,w.polarity)


subdf = pd.DataFrame({'Trump':s,'Hillary':s2,'Bernie':s3})
poldf = pd.DataFrame({'Trump':p,'Hillary':p2,'Bernie':p3})
poldf.plot()
subdf.plot()

lecture_5_problem_1.py
Long ago
Apr 22, 2018

You uploaded an item
Text
lecture_5_problem_1.py
import pip
pip.main(['install','numpy'])
pip.main(['install','pandas'])
import numpy as np
import pandas as pd
pip.main(['install','matplotlib'])
import matplotlib.pyplot as plt
import json
import pip
pip.main(["install","twitter"])
pip.main(["install","textblob"])
from textblob import TextBlob

import twitter
from twitter import Twitter
from twitter import OAuth
from twitter import TwitterHTTPError
from twitter import TwitterStream
from pandas.io.json import json_normalize

from textblob import TextBlob



ck = '4utyWgvDx6HziBbOOMrk9A8Zx'
cs = 'bOulyl2Uac0hGayZSDwrZm1o2ULkTZMLUYubOmEXSkwjPhYVJy'
at = '824423500991660032-6mBuL78cft4sIPx0dnEYrKiDNjIXZz1'
ats = 'fvg7ptaTu9cD5OqAYjCE4cIn3REDjOy6Fv8TP24aHCguD'

oauth = OAuth(at,ats,ck,cs)
api = Twitter(auth=oauth)

q = 'McMaster'

search_results = api.search.tweets(q=q,count = 100)
df = json_normalize(search_results, 'statuses')



s = np.empty(1)
p = np.empty(1)

#df = pd.DataFrame()

for x in df['text']:
    w = TextBlob(x)
    w.sentiment
    s=np.append(s,w.subjectivity)
    #print(w.subjectivity)
    p=np.append(p,w.polarity)



df2 = pd.DataFrame({'subjectivity':s,'polarity':p})
df2.plot()


df['polarity']=p[1:101]
hidf = df[df['polarity']>=.7]
hisn=json_normalize(hidf['entities'],'user_mentions')
