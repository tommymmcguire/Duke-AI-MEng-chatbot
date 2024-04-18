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
    response["response"] = clean_response(response["response"])
    return response


def clean_response(response: str):
    if '###' not in response:
        answer = response
        print('answer1: ', answer)
    else:
        response = None
        output = None
        explanation = None
        # Get the first response, output, and explanation
        l=[]
        if len(response.split('###'))<=2:
            l=response.split('###')
        else:
            l=response.split('###')[:-1]
        # print(l)
        for i in l:
            if i.startswith(' Response') and response is None:
                response = i
            if i.startswith(' Output') and output is None:
                output = i
            if i.startswith(' Explanation') and explanation is None:
                explanation = i

        # Strip them all and remove the prefix
        if response:
            response = response.replace('Response:', '')
            response = response.strip()
        if output:
            output = output.replace('Output:', '')
            output = output.strip()
        if explanation:
            explanation = explanation.replace('Explanation:', '')
            explanation = explanation.strip()

        # Compare if they are the same string

        # Create one long string to return
        if answer == None:
            answer = ''
        if response == None:
            response = ''
        if output == None:
            output = ''
        if explanation == None:
            explanation = ''
        if response == explanation == output:
            answer = response
        elif response == output:
            answer = output + ' ' + explanation
        elif response == explanation:
            answer = output + ' ' + explanation
        elif output == explanation:
            answer = output + ' ' + response
        else:
            answer = response + ' ' + output + ' ' + explanation
    return answer