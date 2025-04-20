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

# Model Details

- **Model**: `sentence-transformers/all-MiniLM-L6-v2`
- **Embedding Dimension**: `384`
- **Max Tokens Per Chunk**: `512`
- **Description**: This model generates dense vector representations of sentences, which can be used for various downstream tasks such as text similarity, clustering, and semantic search.


## API Endpoints

### 1. `/health` (GET)

- **Description**: This endpoint checks the health status of the API.
- **Response**:

```json
{
  "status": "ok"
}
```

### 2. `/info` (GET)

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
### 3. `/embed` (POST)

This endpoint generates sentence embeddings for one or more input text(s). You can provide either a single sentence or a list of sentences. The embeddings are generated using the `sentence-transformers/all-MiniLM-L6-v2` model.

## Request

- **Method**: `POST`
- **URL**: `/embed`
- **Content-Type**: `application/json`
- **Headers**:
  - `x-api-key`: Your API key (replace with your own key)

### Request Body (Example with a list of strings)

```json
{
  "text": [
    "This is the first sentence.",
    "Here is another sentence for embedding.",
    "And this is the third sentence."
  ]
}
```
## Expected Response

```json
{
  "embeddings": [
    [0.123456, 0.234567, 0.345678, ..., 0.987654],
    [0.223344, 0.445566, 0.556677, ..., 0.876543],
    [0.112233, 0.334455, 0.556677, ..., 0.998877]
  ],
  "input_count": 3,
  "dimension": 384
}
```

