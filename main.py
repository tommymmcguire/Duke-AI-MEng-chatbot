from scripts.embed_query import embed_query
from scripts.get_similar_chunks import get_similar_chunks
from scripts.connect_to_LLM import connect_and_query_LLM
from scripts.check_cache import query_cache

def main(query: str):
    # Check the cache for similar quieries
    top_cache_results = query_cache(query, threshold=0) 
    if top_cache_results[0][1] > 0.95:
        rag_output = top_cache_results[0][0]
        return {'rag_output': rag_output, 'response_time': -1}
    
    # If the query is not in the cache, query the model
    embedding = embed_query(query)
    similar_chunks = get_similar_chunks(embedding, top_k=1)
    try:
        rag_output_dict = connect_and_query_LLM(query, similar_chunks)
        if "error" in rag_output_dict.keys():
            rag_output = rag_output = "The model is warming up, please try again in a few minutes."
            response_time = -1
        else:
            rag_output = rag_output_dict['response']
            response_time = rag_output_dict['time']
    except Exception as e:  
        rag_output = f"An error occurred: {e}"

    # Verify that the response is not empty
    if rag_output == "":
        rag_output = top_cache_results[0][0]
        response_time = -2

    return {'rag_output': rag_output, 'response_time': response_time}

if __name__ == "__main__":
    response = main(query="Tell me about Duke University.")
    print(response)