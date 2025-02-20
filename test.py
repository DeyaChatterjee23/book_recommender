import pickle

def test_pickle(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
        print(f"Successfully loaded: {file_path}")
    except Exception as e:
        print(f"Error loading {file_path}: {e}")

test_pickle('/Users/deyachatterjee/Desktop/Book_recommender/pickles/model.pkl')
test_pickle('pickles/book_names.pkl')
test_pickle('pickles/final_rating.pkl')
test_pickle('pickles/book_pivot.pkl')
test_pickle('pickles/similarity_scores.pkl')

