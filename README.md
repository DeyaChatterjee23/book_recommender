# Book Recommender System

![Book Recommendations](https://img.shields.io/badge/Recommendations-Hybrid_Approach-blue)

A hybrid book recommendation system combining collaborative filtering and content-based approaches to suggest books based on user preferences and textual content.

## Features

- **📊 Collaborative Filtering**  
  Uses K-Nearest Neighbors (KNN) to recommend books based on user ratings
  - Filters users with 200+ ratings and books with 50+ ratings
  - Pivot-table based user-item matrix for similarity calculations

- **📝 Content-Based Recommendation**  
  Leverages text embeddings (Gemma2 model) and FAISS for efficient similarity search
  - Analyzes titles, authors, descriptions, and categories
  - Local LLM integration through Ollama

### Collaborative Filtering 
- [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)
  - `BX-Books.csv`: Book metadata (ISBN, title, author, year, etc.)
  - `BX-Users.csv`: User demographics
  - `BX-Book-Ratings.csv`: 1M+ user-book ratings

### Content-Based
This approach uses semantic similarity between book descriptions and metadata to recommend books with similar content, themes, or characteristics rather than relying on user ratings or collaborative filtering.
Dataset:
- `7kbooks.csv` (included in repo)
  - 7,000 books with detailed metadata
  - Titles, authors, descriptions, categories, etc
Workflow:
Data Loading and Preparation:

Imports pandas and loads a CSV file containing information about 7,000 books
Creates a text representation for each book by combining fields like title, authors, description, categories, publishing year, rating, and page count into a single string


Vector Embedding Creation:

Uses FAISS (Facebook AI Similarity Search) library for efficient similarity search
Creates a 2304-dimensional vector space for the book embeddings
For each book, sends its textual representation to a local Ollama API endpoint running the Gemma 2B language model to generate vector embeddings
Stores these embeddings in a FAISS index for efficient similarity search
Saves the index to disk


Recommendation Generation:

Loads a specific book (e.g. index 4533) as the "favorite" book to find similar recommendations
Gets the embedding for this favorite book
Uses FAISS to find the 10 most similar books based on embedding similarity (nearest neighbors in the vector space)
Prints out the textual representations of these similar books




