import numpy as np
import pandas as pd
import pip
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
from matplotlib import pyplot as plt

data = fetch_movielens(min_rating=4)


model=LightFM(loss='warp')
model.fit(data['train'],epochs=30,num_threads=2)

n_users, n_items=data['train'].shape

scores=model.predict(0,np.arange(n_items))
top_items=data['item_labels'][np.argsort(-scores)]


userids = np.arange(n_users)
s = np.empty(0)

v=np.array(0)
for u in userids:
    scores=model.predict(u,np.arange(n_items))
    ss = np.argsort(-scores)
    top_items=data['item_labels'][ss[0]]
    s=np.append(s,top_items)

df = pd.DataFrame({'movie':s})
df.groupby('movie')['movie'].size().sort_values(ascending=False).head(30).plot(kind='bar')
v=np.array(0)
pos = data['item_labels'][data['train'].tocsr()[0].indices]
pos = data['item_labels'][data['train'].tocsr()[7].indices]
cnt1=0
for u in userids:
    pos=data['item_labels'][data['train'].tocsr()[u].indices]
    for r in pos:
        if r=="Raiders of the Lost Ark (1981)":
            v=np.append(v,r)
            cnt1=cnt1+1
cnt2=0        
for u in userids:
    pos=data['item_labels'][data['train'].tocsr()[u].indices]
    for r in pos:
        if r=="Godfather, The (1972)":
            v=np.append(v,r)
            cnt2=cnt2+1
            
cnt3=0         
for u in userids:
    pos=data['item_labels'][data['train'].tocsr()[u].indices]
    for r in pos:
        if r=="Gumby: The Movie (1995)":
            v=np.append(v,r)
            cnt3=cnt3+1

print(cnt1)
print(cnt2)
print(cnt3)
df2 = pd.DataFrame(cnt1,cnt2,cnt3)
df.groupby('movie')['movie'].size().sort_values(ascending=False).head(30).plot(kind='bar')


