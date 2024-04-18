import os
import torch
from langchain.text_splitter import CharacterTextSplitter
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec

'''
Embedder class is responsible for embedding the text chunks using a specified embedding model.
It has methods for embedding a list of text chunks and returning the embeddings.

Parameters: 
model_name - name of the embedding model to use, default is avsolatorio/GIST-Embedding-v0

Return: list of embeddings
'''
class Embedder:
    def __init__(self, model_name="avsolatorio/GIST-Embedding-v0"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def embed_text_chunks(self, chunks):
        embeddings = []
        for chunk in chunks:
            # Tokenize the chunk and add special tokens at the beginning and end
            inputs = self.tokenizer(chunk, return_tensors="pt", padding=True, truncation=True, max_length=512)
            # Pass the tokenized inputs to the model
            with torch.no_grad():
                outputs = self.model(**inputs)
            # Get the embeddings from the last hidden state
            # The output depends on your specific requirements, you might want to average the token embeddings
            chunk_embeddings = outputs.last_hidden_state.mean(dim=1)
            embeddings.append(chunk_embeddings)
        return embeddings
    
'''
PineconeIntegration class is responsible for creating and uploading embeddings to Pinecone.
It has methods for creating an index and uploading embeddings.

Parameters: 
name - name of the index to create, default is 'gist-embedding'
dimension - dimension of the embeddings, default is 768
metric - metric to use for similarity search, default is 'cosine'
embeddings - list of embeddings to upload
chunks - list of text chunks corresponding to the embeddings

Return: None
'''
class PineconeIntegration:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("PINECONE_API_KEY")
        self.pc = Pinecone(api_key=self.api_key)

    def create_index(self, name='gist-embedding', dimension=768, metric='cosine'):
        if name not in self.pc.list_indexes().names():
            self.pc.create_index(name=name, dimension=dimension, metric=metric,
                                 spec=ServerlessSpec(cloud='aws', region='us-west-2'))

    def format_embeddings(self, embeddings, chunks):
        # Format the embeddings for Pinecone
        formatted_embeddings_gist = [{"id": str(i), "values": emb.tolist(), "metadata": {"text": text}} for i, (emb, text) in enumerate(zip(embeddings, chunks))]
        return formatted_embeddings_gist

    def upload_embeddings(self, index_name, embeddings):
        index = self.pc.Index(index_name)
        batch_size = 100
        for i in range(0, len(embeddings), batch_size):
            batch = embeddings[i:i + batch_size]
            index.upsert(vectors=batch)

if __name__ == "__main__":
    # Load chunks 
    all_chunks = []

    # Create an instance of the Embedder and embed the text chunks.
    # The default embedding model is avsolatorio/GIST-Embedding-v0, if you want to use a different model, specify the model name in the Embedder constructor.
    embedder = Embedder()
    chunk_embeddings = embedder.embed_text_chunks(all_chunks)

    pinecone_integration = PineconeIntegration()
    pinecone_integration.create_index()
    formatted_embeddings = pinecone_integration.format_embeddings(chunk_embeddings, all_chunks)
    pinecone_integration.upload_embeddings('gist-embedding', formatted_embeddings)