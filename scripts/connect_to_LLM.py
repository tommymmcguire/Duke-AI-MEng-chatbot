import os
import requests
from dotenv import load_dotenv


'''
This script connects to our LLM, passes in the top n chunks, and returns the response.
'''

'''
Connects to LLM and generates response given the most similar chunks.

Parameters:
top_similarities - dictionary of chunks and their similarity scores
query - query to match
top_n - number of chunks to try and use

Returns:
Response from the LLM (string) 
'''
def connect_and_prompt_LLM_RAG(top_similarities, query, top_n=5):
    pass


def connect_and_query_LLM(query):
    load_dotenv()
    API_URL = "https://jxwi0y7vmmxdev9v.us-east-1.aws.endpoints.huggingface.cloud"
    headers = {
	"Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
	"Content-Type": "application/json" 
    }
    payload = {
        "inputs": query
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

if __name__ == "__main__":
    input = {"context": "Duke University AI Masters of Engineering program has a 1-year track.", 
             "question": "Can I complete the Duke University AI Masters of Engineering program in 1 year?"}
    output = connect_and_query_LLM(
        {
            "inputs": f"given this context: {input['context']} and this question: {input['question']} what is the answer?"
        }
    )
    print(output)