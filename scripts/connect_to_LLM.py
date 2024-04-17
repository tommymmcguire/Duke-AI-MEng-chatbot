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
def connect_and_prompt_LLM_RAG(top_similarities, query, top_n=3):
    pass


def connect_and_query_LLM(query, top_similarities):
    load_dotenv()
    API_URL = "https://jxwi0y7vmmxdev9v.us-east-1.aws.endpoints.huggingface.cloud"
    headers = {
	"Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
	"Content-Type": "application/json" 
    }
    payload = {
         "inputs": { "instruction": f"Given the information about Duke's AI MEng program,please answer the following query in great detail, but succinct.",
                   "query": f"INFORMATION: { top_similarities} QUERY: {query} "
                   }

          #If the passed in information is not relevant, please say the exact phrase: `I don't know`. Check that the response actually addresses the query. If it does not, please try again."
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()