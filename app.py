import streamlit as st
import pickle

st.title("Movie Recommender System")

movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or Select a movie from DropDown",movie_list
)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


if st.button("Recommend Movie"):
    recomendations = recommend(selected_movie)
    for i in recomendations:
        st.write(i)
