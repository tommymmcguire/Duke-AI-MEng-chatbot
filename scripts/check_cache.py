import numpy as np
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.embed_query import embed_query
import json
import time

#function that computes cosine similarity between two vectors
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

#function that returns answer if the cosine similarity is greater than 0.5
def get_similar_chunks(query_embedding, top_n=3, threshold=0.95):
    with open('data/questions_embedded.jsonl', 'r') as file:
        similarities = {}
        for line in file:
            data = json.loads(line)
            question = data['question']
            embedding = data['embedding']
            answer = data['answer']
            similarity = cosine_similarity(query_embedding, embedding)
            similarities[answer] = similarity
        # get top n answers with the highest similarity above the threshold as a list
        top_similarities = []
        for answer, similarity in sorted(similarities.items(), key=lambda x: x[1], reverse=True):
            if similarity > threshold:
                top_similarities.append((answer,similarity))
            if len(top_similarities) == top_n:
                break
        return top_similarities

def query_cache(query, threshold=0.95):
    query_embedding = embed_query(query)
    top_similarity_scores = get_similar_chunks(query_embedding, top_n=1, threshold=threshold)
    return top_similarity_scores

    