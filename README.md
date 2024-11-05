Movie Recommendation System
This is a web application that recommends movies based on the user's input. The application features an interactive frontend connected to a backend service that provides movie recommendations and additional movie details.

Table of Contents
About the Project
Features
Project Structure
Data Requirements
Getting Started
Prerequisites
Installation
Usage
Built With
Acknowledgments
About the Project
The Movie Recommendation System is designed to help users discover new movies based on their preferences. By entering a movie title, users receive a list of similar or recommended movies. Each recommendation is clickable, allowing users to see more detailed information such as genre, director, cast, and an overview.

Features
Top 10 Similar Movies: Recommends the top 10 movies similar to the user’s favorite.
Cosine Similarity Calculation: Uses cosine similarity to calculate movie similarity based on selected features.
Error Handling: Handles user input errors by finding the closest match to the entered movie name.
Textual Data Processing: Works with textual movie data to create feature vectors and compare them numerically.
Interactive UI: Recommendations are presented with an appealing, responsive design.
Modal Display: Each movie recommendation provides additional details (e.g., genres, director, cast) in a popup modal.
Dynamic Styling: The frontend includes dynamic and visually engaging styling with animations and overlays for an enhanced user experience.
Project Structure
The project consists of the following main components:

Frontend:
HTML (index.html): Sets up the structure of the web page, including the form for user input and the section for displaying recommendations.
CSS (style.css): Defines the look and feel of the application, with styling for layout, colors, animations, and responsiveness.
Backend:
Python (web.py): Handles server-side operations, processing requests for movie recommendations and fetching detailed information about each movie.
Data Requirements
The code requires a CSV file with movie data, containing the following columns:

genres
keywords
tagline
cast
director
overview
original_language
title
index
Getting Started
To get a local copy of this project up and running, follow these steps.

Prerequisites
Python 3.x
Required libraries:
numpy
pandas
sklearn
difflib
scikit-learn
Installation
Clone the repository:
sh
Copy code
git clone https://github.com/your-username/Movie-Recommendation-System.git
Navigate to the project directory:
sh
Copy code
cd Movie-Recommendation-System
Install the required dependencies:
sh
Copy code
pip install -r requirements.txt
Start the backend server:
sh
Copy code
python web.py
Open index.html in a web browser to access the frontend.
Usage
Open the application in your web browser.
Type the name of a movie in the input field and click "Get Recommendations."
A list of recommended movies will appear below the input form.
Click on any movie title to view more details in a modal popup.
Built With
HTML/CSS for frontend structure and styling.
JavaScript for dynamic interaction in the frontend.
Flask (Python) for backend functionality.
Machine Learning Libraries: numpy, pandas, and scikit-learn for processing and calculating similarity.
Acknowledgments
Special thanks to online movie databases for providing API access to movie information.
This project was developed as part of a self-study project to enhance frontend and backend integration skills.