from flask import Flask, render_template, request, jsonify
import pickle
import requests
import pickle

app = Flask(__name__)

# Fetch movie poster from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path', '')
    return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "https://via.placeholder.com/200"

# Load movie data
movies = pickle.load(open("/Users/ranawatprajinrajbhavesh/Desktop/THIS PC/CODES/Flask/movies_list.pkl", 'rb'))
similarity = pickle.load(open("/Users/ranawatprajinrajbhavesh/Desktop/THIS PC/CODES/Flask/similarity.pkl", 'rb'))
movies_list = movies['title'].values

# Home route
@app.route('/')
def index():
    sample_posters = [fetch_poster(movie_id) for movie_id in [1632, 299536, 17455, 2830, 429422, 9722, 13972, 240, 155, 598, 914, 255709, 572154]]
    return render_template("index.html", movies=movies_list, sample_posters=sample_posters)

# Recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form.get("movie")
    index = movies[movies['title'] == movie_name].index[0]
    
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    recommended_posters = []

    for i in distances[1:6]:  # Top 5 recommendations
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    
    return jsonify({'movies': recommended_movies, 'posters': recommended_posters})

if __name__ == "__main__":
    app.run(debug=True)

