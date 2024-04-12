from sentence_transformers import SentenceTransformer

'''
This script is responsible for embedding the query and returning the embeddings.
'''

'''
Embed query using the GIST-Embedding-v0 model.

Parameters:
query - query to embed
model_name - name of the model to use, default is 'avsolatorio/GIST-Embedding-v0'

Return:
embedding - embedding of the query
'''
def embed_query(query, model_name='avsolatorio/GIST-Embedding-v0'):
    # Initialize the SentenceTransformer
    model = SentenceTransformer(model_name)

    # Embed the query
    embedding = model.encode([query], convert_to_tensor=True)

    # Convert embedded query tensor to list before querying the index
    embedding = embedding[0].squeeze().tolist()

    return embedding