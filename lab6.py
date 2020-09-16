import json
import pip
pip.main(["install","yelp"])

ckey = "DxWcdDWDAY8TeUfW1c6XLQ"
csecret = "VbOYpTA-60i-U1GqeRlSU6qcjL8"
token = "34gFepoCHayRLEctZuFaDpiapJ-NEe1D"
tokensecret = "rCW8MCDdiH4TLZIpBP9IN8TdVZ8"

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from pandas.io.json import json_normalize
import numpy as np
import pandas as pd

auth = Oauth1Authenticator(
    consumer_key=ckey,
    consumer_secret=csecret,
    token=token,
    token_secret=tokensecret
)

api = Client(auth)
params = {"term":"sushi","lang":"en","limit":200,"offset":0,"sort":1}
val = api.search("Newark, NJ",params)
val.businesses
val.businesses[0].name

df2 = pd.DataFrame()

for v in val.businesses:
    r =pd.Series([v.name,v.id,v.rating,v.review_count])
    df2 = df2.append(r, ignore_index=True)

df2.columns = ['name','id','rating','count']

df2.plot(kind="bar",x="name",y="rating")
df2.plot(kind="bar",x="name",y="count",color="pink")

#id = val.businesses[0].id

#nn = api.get_business(fid)


