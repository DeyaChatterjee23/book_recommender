import pickle
import streamlit as st
import numpy as np


st.header("Book Recommender")
st.write("Loading files...")
#import all pickle files
try:
    model = pickle.load(open('/Users/deyachatterjee/Desktop/Book_recommender/pickles/model.pkl', 'rb'))
    st.write("Model file loaded successfully.")
except Exception as e:
    st.error(f"Error loading model.pkl: {e}")

try:
    book_names = pickle.load(open('pickles/book_names.pkl', 'rb'))
    st.write("Book names file loaded successfully.")
except Exception as e:
    st.error(f"Error loading book_names.pkl: {e}")

try:
    final_rating = pickle.load(open('pickles/final_rating.pkl', 'rb'))
    st.write("Final rating file loaded successfully.")
except Exception as e:
    st.error(f"Error loading final_rating.pkl: {e}")

try:
    book_pivot = pickle.load(open('pickles/book_pivot.pkl', 'rb'))
    st.write("Book pivot file loaded successfully.")
except Exception as e:
    st.error(f"Error loading book_pivot.pkl: {e}")

try:
    similarity_scores = pickle.load(open('pickles/similarity_scores.pkl', 'rb'))
    st.write("Similarity scores file loaded successfully.")
except Exception as e:
    st.error(f"Error loading similarity_scores.pkl: {e}")
# try:
#     model=pickle.load(open('pickles/model.pkl', 'rb'))
#     book_names=pickle.load(open('pickles/book_names.pkl', 'rb'))
#     final_rating=pickle.load(open('pickles/final_rating.pkl', 'rb'))
#     book_pivot=pickle.load(open('pickles/book_pivot.pkl', 'rb'))
#     similarity_scores=pickle.load(open('pickles/similarity_scores.pkl', 'rb'))
#     st.write("Pickles loaded succesfully")
# except Exception as e:
#     st.write(f"{e}")
#     st.error(f"Error loading model.pkl: {e}")
    

def fetch_poster(suggestion):
    book_name= []
    ids_index = []
    poster_url = []


    for bid in suggestion:
        book_name.append(book_pivot.index[bid])
    
    for name in book_name:
        if len(np.where(final_rating['title'] == name)[0]) > 0:
            ids = np.where(final_rating['title']== name)[0][0]
            ids_index.append(ids)
    
    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url

def recommender(book_name):
    book_list= []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1,-1), n_neighbors=6)
    poster_url = fetch_poster(suggestion[0])
    books = list(book_pivot.index[suggestion[0]])
    
    return books, poster_url



selected_book= st.selectbox("Select from the list of books", book_names)


if st.button('Generate recommendations'):
    
    recommendations, poster_url = recommender(selected_book)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(recommendations[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommendations[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommendations[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommendations[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommendations[5])
        st.image(poster_url[5])