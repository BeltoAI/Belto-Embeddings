# Sentence Embedding API with Quart

This project provides an API for generating sentence embeddings using the **Sentence-Transformers** model. The API is built using the **Quart** framework, allowing for asynchronous operations and CORS support. The embedding process is powered by the `sentence-transformers/all-MiniLM-L6-v2` model, which is capable of transforming input text into numerical vectors (embeddings) for various use cases like text similarity, clustering, and search.

## Libraries Used

- **Quart**: An asynchronous Python web framework that is compatible with Flask. It's used for building the API.
- **Sentence-Transformers**: A library for generating embeddings from pre-trained models like `all-MiniLM-L6-v2`. This library simplifies working with transformer models for sentence-level embeddings.
- **Transformers**: A library from Hugging Face for pre-trained transformer models like BERT, GPT, etc.
- **Numpy**: A library used for numerical operations, particularly in normalizing the embeddings for better cosine similarity computations.

## Use Cases

- **Text Similarity**: Find the similarity between sentences or documents by comparing their embeddings.
- **Clustering**: Group similar sentences together by comparing their embeddings.
- **Search**: Perform semantic search by matching query embeddings to document embeddings.
- **Recommendation Systems**: Recommend similar sentences or documents based on embeddings.

## API Endpoints

### 1. `/health` (GET)

- **Description**: This endpoint checks the health status of the API.
- **Response**:

```json
{
  "status": "ok"
}
```

## API Endpoint: `/info` (GET)

This endpoint provides information about the model and its configuration.

### Response

```json
{
  "description": "Embeds text input using Sentence Transformers.",
  "embedding_dimension": 384,
  "max_tokens_per_chunk": 512,
  "model": "sentence-transformers/all-MiniLM-L6-v2"
}
```
