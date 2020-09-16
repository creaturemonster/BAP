oauth = OAuth(at,ats,ck,cs)
api = Twitter(auth=oauth)

q = 'terrorism'

search_results = api.search.tweets(q=q,count = 100)
df = json_normalize(search_results, 'statuses')

s = np.empty(1)
p = np.empty(1)

for x in df['text']:
    w = TextBlob(x)
    w.sentiment
    s=np.append(s,w.subjectivity)
    #print(w.subjectivity)
    p=np.append(p,w.polarity)

df2 = pd.DataFrame({'subjectivity':s,'polarity':p})
df2.plot()
