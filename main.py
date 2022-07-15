import pickle
import  pandas as pd
import streamlit as st
import requests

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=6b2a5035bf2cf3393eb1240e618f1555&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movie_list[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

st.title('Movies Recommender System')

selected_movie_name = st.selectbox(
     'How would you like to be contacted?',
     (movies['title'].values))

if st.button('Recommend'):
   names , poster = recommend(selected_movie_name)
     # for i in recommendations: st.write(i)
   col1, col2, col3, col4 , col5  = st.columns(5)

   with col1:
       st.text(names[0])
       st.image(poster[0])

   with col2:
       st.text(names[1])
       st.image(poster[1])

   with col3:
       st.text(names[2])
       st.image(poster[2])
   with col4:
        st.text(names[3])
        st.image(poster[3])
   with col5:
         st.text(names[4])
         st.image(poster[4])



