import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title']

st.header('Movie Recommendation System')
select = st.selectbox("Select Movies From Below Movies List",movies_list)

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=47a25904d9c6a8eb3dfb83e2ed01097e&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
    return full_path

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key=lambda x:x[1])
    recommend_movies=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movies, recommend_poster

if st.button('Show Recommended Movies'):
    movies_rec, movie_poster = recommend(select)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(movies_rec[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movies_rec[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movies_rec[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movies_rec[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movies_rec[4])
        st.image(movie_poster[4])