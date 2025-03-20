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

## Dataset

### Collaborative Filtering
- [Book-Crossing Dataset](http://www2.informatik.uni-freiburg.de/~cziegler/BX/)
  - `BX-Books.csv`: Book metadata (ISBN, title, author, year, etc.)
  - `BX-Users.csv`: User demographics
  - `BX-Book-Ratings.csv`: 1M+ user-book ratings

### Content-Based
- `7kbooks.csv` (included in repo)
  - 7,000 books with detailed metadata
  - Titles, authors, descriptions, categories, ratings




