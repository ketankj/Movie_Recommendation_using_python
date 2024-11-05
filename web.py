from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

# Initialize Flask app
app = Flask(__name__)

# Load movie data
movies_data = pd.read_csv('movies.csv')

# Select relevant features for recommendations
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director', 'overview', 'original_language']

# Fill NaN values with empty string
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

# Combine all selected features into a single string
movies_data['combined_features'] = movies_data[selected_features].apply(lambda x: ' '.join(x), axis=1)

# Convert the text data to feature vectors
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(movies_data['combined_features'])

# Define a route to handle movie search and return recommendations
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name']

    # Find the closest match for the movie title using difflib
    list_of_all_titles = movies_data['title'].tolist()
    close_matches = difflib.get_close_matches(movie_name, list_of_all_titles)
    
    if close_matches:
        best_match = close_matches[0]
        index_of_movie = movies_data[movies_data.title == best_match].index[0]

        # Calculate cosine similarity
        similarity = cosine_similarity(feature_vectors)

        # Get similarity scores for the movie
        similarity_scores = list(enumerate(similarity[index_of_movie]))
        sorted_similar_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        
        recommended_movies = []
        for i in sorted_similar_movies[1:11]:  # Top 10 movies
            movie_index = i[0]
            recommended_movies.append(movies_data['title'].iloc[movie_index])

        return jsonify(recommended_movies)
    else:
        return jsonify([])

# New route to fetch detailed movie information
@app.route('/movie_info', methods=['POST'])
def movie_info():
    movie_title = request.form['title']

    # Find the movie in the dataset
    movie_data = movies_data[movies_data['title'] == movie_title].to_dict(orient='records')

    if movie_data:
        return jsonify(movie_data[0])  # Return the first match
    else:
        return jsonify({'error': 'Movie not found'})

if __name__ == '__main__':
    app.run(debug=True)
