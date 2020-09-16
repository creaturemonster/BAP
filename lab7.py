import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('C:/Users/RGunda200/Desktop/Rahul/MBA/Spring-2017/Business_Analytics_Programming/Lab_Submitted/ml-100k/ml-100k/u.user', sep='|', names=u_cols, encoding='latin-1')
users[:25]
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('C:/Users/RGunda200/Desktop/Rahul/MBA/Spring-2017/Business_Analytics_Programming/Lab_Submitted/ml-100k/ml-100k/u.data', sep='|', names=r_cols,encoding='latin-1')
ratings[:25]
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('C:/Users/RGunda200/Desktop/Rahul/MBA/Spring-2017/Business_Analytics_Programming/Lab_Submitted/ml-100k/ml-100k/u.item', sep='|', names=m_cols,encoding='latin-1')
movies[:25]
df= pd.DataFrame(pd.merge(pd.merge(ratings,users),movies))
movie_ratings = pd.merge(movies, ratings)
lens = pd.merge(movie_ratings, users)
most_rated = lens.groupby('title').size().sort_values(ascending=False)[:25]
most_rated=most_rated[np.isnan(most_rated)]
most_rated
movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
for (most_rated,movie_stats) in movie_ratings.groupby('rating'):
    print("{0:30} shape={1}".format(most_rated,movie_data))
    
movie_stats.head()
movie_stats.sort_values([('rating', 'mean')], ascending=False).head()
atleast_100 = movie_stats['rating']['size'] >= 100
movie_stats[atleast_100].sort_values([('rating', 'mean')], ascending=False)[:15]
movies.title.plot.hist(bins=30)
movie_data = pd.merge(movies,pd.merge(ratings,users))
movie_data.drop_duplicates(subset='movie_id').sort('rating', ascending = False).head(5)
plt.title("Distribution of the top recommended movies by users")
plt.ylabel("Frequency")
plt.xlabel("titles")
users.age.plot.hist(bins=30)
plt.title("Distribution of users' ages")
plt.ylabel('count of users')
plt.xlabel('age')
    
