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
         "inputs": { "instruction": f"Given the INFORMATION about Duke's AI MEng program, please answer the following QUERY in great detail using facts from the INFORMATION. Answer with a full sentence.",
                   "query": f"INFORMATION: { top_similarities} QUERY: {query} "
                   }

          #If the passed in information is not relevant, please say the exact phrase: `I don't know`. Check that the response actually addresses the query. If it does not, please try again."
    }
    response = requests.post(API_URL, headers=headers, json=payload).json()
    print("Raw response from LLM: \n")
    print(response)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    response["response"] = filter_response(response["response"])
    return response


def filter_response(response: str):
    stripped = response.strip()
    # See if a response is there, if so use it.     
    split_result = (stripped.split('###'))     
    if split_result[0].strip() != '':         
        print('Response Found: ', split_result[0])         
        return split_result[0].strip()     
    else:         # Look for next ### and return that as the response         
        print('Seconod Reponse: ', split_result[1].split(':', 1)[1])         
        return split_result[1].split(':', 1)[1].strip()