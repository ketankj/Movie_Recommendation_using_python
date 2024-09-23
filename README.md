# Movie_Recomendation_using Python
Movie Recommendation System
This repository contains a Python-based movie recommendation system that suggests movies similar to the one entered by the user. The system is powered by content-based filtering, leveraging features like genres, keywords, cast, and more to calculate similarity scores and recommend movies.

Features:
Recommends the top 10 movies similar to the user’s favorite.
Uses cosine similarity to calculate movie similarity based on selected features.
Handles user input errors by finding the closest match to the entered movie name.
Works with textual movie data to create feature vectors and compare them numerically.
Data Requirements:
The code requires a CSV file with movie data, including the following columns:
genres
keywords
tagline
cast
director
overview
original_language
title
index
Prerequisites:
Python 3.x
Required libraries:
numpy
pandas
sklearn
difflib
scikit-learn
Installation:
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
Install the required Python libraries:

bash
Copy code
pip install numpy pandas scikit-learn
Ensure your dataset is in CSV format (movies.csv), and place it in the same directory as the script.

Usage:
Make sure your dataset is correctly formatted (with the necessary columns as listed above).

Run the Python script:

bash
Copy code
python movie_recommender.py
The system will prompt you to enter your favorite movie. Based on the closest match, it will recommend the top 10 similar movies.

Example input:

mathematica
Copy code
Enter your favorite movie name: Inception
The system will display something like:

markdown
Copy code
Top 10 movies suggested for you:
1. Interstellar
2. The Matrix
3. The Prestige
...
Customization:
You can modify the interval for fetching similar movies by changing the similarity score threshold.
Adjust the input feature set by modifying the selected_features list in the code.
