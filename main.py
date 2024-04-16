from scripts.embed_query import embed_query
from scripts.get_similar_chunks import get_similar_chunks
from scripts.connect_to_LLM import connect_and_query_LLM

def main():
    query = "Can you complete the AI Masters program in 1 year?"
    query_embedding = embed_query(query)
    top_similarity_scores = get_similar_chunks(query_embedding)
    response = connect_and_query_LLM(query, top_similarity_scores)
    print(response)
    return response

if __name__ == "__main__":
    main()