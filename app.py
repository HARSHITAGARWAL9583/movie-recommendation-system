# from http.client import responses
#
# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     responses = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#     data = responses.json()
#     st.text(data)
#     st.text
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         #fetch poster
#
#         recommended_movies.append(movies.iloc[i[0]].title)
#         # fetch poster
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies
#
# # Load data
# movies_dict = pickle.load(open('movie_dict.pkl','rb'))
# movies = pd.DataFrame(movies_dict)
# similarity = pickle.load(open('similarity.pkl','rb'))
#
# # App title
# st.title('Movie Recommender System')
#
# # Dropdown
# selected_movie_name = st.selectbox(
#     'Select a movie:',
#     movies['title'].values
# )
#
# # Button
# if st.button('Recommend'):
#     names,posters= recommend(selected_movie_name)
#
#     col1, col2, col3,col4,col5 = st.beta_columns(5)
#
#     with col1:
#         st.header(names[0])
#         st.image(posters[0])
#
#     with col2:
#         st.header(names[1])
#         st.image(posters[1])
#
#     with col3:
#         st.header(names[2])
#         st.image(posters[2])
#     with col4:
#         st.header(names[3])
#         st.image(posters[3])
#     with col5:
#         st.header(names[4])
#         st.image(posters[4])
#
#
#


import streamlit as st
import pickle
import pandas as pd
import requests

# ✅ Function to fetch poster from TMDB API
def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    )
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"

# ✅ Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# ✅ Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ✅ Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])