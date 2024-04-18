import numpy as np
from embed_query import embed_query
import json
import time

#function that computes cosine similarity between two vectors
def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

#function that returns answer if the cosine similarity is greater than 0.5
def get_similar_chunks(query_embedding, top_n=3, threshold=0.87):
    with open('data/questions_embedded.jsonl', 'r') as file:
        similarities = {}
        for line in file:
            data = json.loads(line)
            question = data['question']
            embedding = data['embedding']
            answer = data['answer']
            similarity = cosine_similarity(query_embedding, embedding)
            similarities[(question,answer)] = similarity
        # get top n answers with the highest similarity above the threshold as a list
        top_similarities = []
        for answer, similarity in sorted(similarities.items(), key=lambda x: x[1], reverse=True):
            if similarity > threshold:
                top_similarities.append((answer,similarity))
            if len(top_similarities) == top_n:
                break
        return top_similarities

if __name__ == "__main__":
    s_time = time.time()
    query = "What are the prerequisites to applying to the program?"
    query_embedding = embed_query(query)
    top_similarity_scores = get_similar_chunks(query_embedding)
    print(top_similarity_scores)
    print(f"Time taken: {time.time() - s_time}")

    