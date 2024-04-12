import os

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
def connect_to_LLM(top_similarities, query, top_n=5):
    pass