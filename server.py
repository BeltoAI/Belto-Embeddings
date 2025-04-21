from quart import Quart, request, jsonify
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer
from functools import wraps
from quart_cors import cors
import numpy as np  # Importing numpy for vector operations
from marshmallow import Schema, fields, ValidationError

# Model and tokenizer initialization
MODEL_NAME = 'sentence-transformers/all-MiniLM-L6-v2'
API_KEY = "123456789012345"  # Replace this with your own secure key

# Load the model once at the application startup
model = SentenceTransformer(MODEL_NAME)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# Initialize app with CORS enabled
app = cors(Quart(__name__), allow_origin="*")  # You can restrict origin to just your frontend domain

# Auth decorator to check for API key
def require_api_key(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        key = request.headers.get('x-api-key')
        if key != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401
        return await func(*args, **kwargs)
    return wrapper

# Input validation schema
class TextInputSchema(Schema):
    text = fields.List(fields.String(), required=True)

# Health check route
@app.route('/health', methods=['GET'])
async def health():
    return jsonify({"status": "ok"})

# Info route to provide model and token information
@app.route('/info', methods=['GET'])
@require_api_key
async def info():
    return jsonify({
        "model": MODEL_NAME,
        "embedding_dimension": model.get_sentence_embedding_dimension(),
        "max_tokens_per_chunk": tokenizer.model_max_length,
        "description": "Embeds text input using Sentence Transformers."
    })

# Embed route for processing text and generating embeddings
@app.route('/embed', methods=['POST'])
@require_api_key
async def embed():
    try:
        data = await request.get_json()

        # Validate input using marshmallow schema
        try:
            validated_data = TextInputSchema().load(data)
        except ValidationError as err:
            return jsonify({"error": f"Invalid input: {err.messages}"}), 400

        texts = validated_data["text"]

        # Input validation checks
        if not texts:
            return jsonify({"error": "Text input cannot be empty"}), 400

        if isinstance(texts, str):
            texts = [texts]
        elif not isinstance(texts, list):
            return jsonify({"error": "'text' must be a string or a list of strings"}), 400

        # Use the preloaded model for inference
        embeddings = model.encode(texts, convert_to_numpy=True)

        # Normalize embeddings (optional, for cosine similarity)
        normalized_embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

        # Convert embeddings to list format for easy handling in JavaScript
        embeddings_list = normalized_embeddings.tolist()

        return jsonify({
            "embeddings": embeddings_list,
            "input_count": len(texts),
            "dimension": model.get_sentence_embedding_dimension()
        })

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Listen on all IP addresses and port 5005
    app.run(host='0.0.0.0', port=5005)
