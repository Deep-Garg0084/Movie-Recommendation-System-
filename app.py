import streamlit as st
import pickle
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

body {
    background-color: #0E1117;
}

.main {
    background-color: #0E1117;
    color: white;
}

.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #FF4B4B;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #CFCFCF;
    margin-bottom: 35px;
}

.stSelectbox label {
    font-size: 20px;
    font-weight: bold;
    color: white;
}

.movie-card {
    background-color: #262730;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 15px;
    font-size: 20px;
    font-weight: 500;
    color: white;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
    transition: 0.3s;
}

.movie-card:hover {
    transform: scale(1.02);
}

.footer {
    text-align: center;
    margin-top: 40px;
    color: gray;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ---------------- #

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------------- RECOMMEND FUNCTION ---------------- #

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

# ---------------- TITLE ---------------- #

st.markdown(
    '<div class="title">🎬 Movie Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Find movies similar to your favorite movie 🍿</div>',
    unsafe_allow_html=True
)

# ---------------- SELECT MOVIE ---------------- #

selected_movie = st.selectbox(
    "Choose a Movie",
    movies['title'].values
)

# ---------------- BUTTON ---------------- #

if st.button("Recommend Movies 🎥"):

    recommendations = recommend(selected_movie)

    st.write("## Recommended Movies")

    for movie in recommendations:

        st.markdown(
            f'<div class="movie-card">⭐ {movie}</div>',
            unsafe_allow_html=True
        )

# ---------------- FOOTER ---------------- #

st.markdown(
    '<div class="footer">Made with ❤️ using Streamlit</div>',
    unsafe_allow_html=True
)