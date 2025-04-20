# Example: Using the API with Cosine Similarity in JavaScript

This example demonstrates how to use the `/embed` API endpoint in JavaScript to obtain sentence embeddings and compute cosine similarity between vectors.

## Code Overview

### 1. **Cosine Similarity Function**

The `cosineSimilarity` function calculates the similarity between two vectors. It computes the dot product of the vectors and divides it by the product of their magnitudes. This function is essential for comparing the similarity between two text embeddings.

```javascript
function cosineSimilarity(vecA, vecB) {
    if (!vecA || !vecB || vecA.length !== vecB.length) {
        console.error('Error: Vectors are of different lengths or null/undefined.');
        return NaN;
    }

    const dotProduct = vecA.reduce((sum, v, i) => sum + v * vecB[i], 0);
    const magnitudeA = Math.sqrt(vecA.reduce((sum, v) => sum + v * v, 0));
    const magnitudeB = Math.sqrt(vecB.reduce((sum, v) => sum + v * v, 0));

    if (magnitudeA === 0 || magnitudeB === 0) {
        console.error('Error: One of the vectors has zero magnitude.');
        return NaN;
    }

    return dotProduct / (magnitudeA * magnitudeB);
}
```
## 2. Fetching Embeddings

The `getEmbedding` function sends a `POST` request to the `/embed` API endpoint to fetch the embedding for a given text. It logs the embedding response and returns the first embedding in the array (assuming only one vector per string).

### Code Example

```javascript
async function getEmbedding(text) {
    try {
        const response = await axios.post('http://localhost:5000/embed', {
            text: text
        }, {
            headers: {
                'x-api-key': '123456789012345' // Replace with your actual API key
            }
        });

        // Debugging: Log the embeddings received from the Python API
        console.log(`Embedding for "${text}":`, response.data.embeddings);

        return response.data.embeddings[0]; // Assuming only one vector per string in the response
    } catch (error) {
        console.error('Error fetching embedding:', error);
        return null;
    }
}
```
