import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

API_KEY = "462011b61ee13f6a8a2ae3c522cbd494"  

movies = pd.read_csv('tmdb_5000_movies.csv')
movies['combined'] = movies['genres'] + ' ' + movies['keywords'] + ' ' + movies['tagline'].fillna('') + ' ' + movies['overview'].fillna('')
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['combined'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
movies = movies.reset_index()
indices = pd.Series(movies.index, index=movies['title'])

def fetch_poster(title):
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={title}"
    response = requests.get(search_url)
    data = response.json()
    if data['results']:
        poster_path = data['results'][0].get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    return "https://via.placeholder.com/300x450?text=No+Image"

def recommend(movie_name):
    if movie_name not in indices:
        return [], []

    idx = indices[movie_name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    movie_indices = [i[0] for i in sim_scores]
    recommended_titles = movies['title'].iloc[movie_indices].tolist()
    recommended_posters = [fetch_poster(title) for title in recommended_titles]
    return recommended_titles, recommended_posters
