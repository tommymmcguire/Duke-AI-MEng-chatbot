from dotenv import load_dotenv
from pinecone import Pinecone
import os

'''
This script is to query the pinecone index for similar chunks to a given query.
'''

'''
Find the top n chunks in the index that are most similar to the query.

Parameters:
query - query to match
index - pinecone index to match (default is "gist")
top_k - number of chunks to return, default is 10

Return:
Dictionary of chunks and their similarity scores
'''
def get_similar_chunks(query, index="gist", top_k=10):
    # Load environment variables from .env file
    load_dotenv()
    # Import the Pinecone client library and connect to Pinecone
    pc = Pinecone(api_key=os.environ.get["PINECONE_API_KEY"])

    # Get the index
    index_name = "gist"
    index = pc.Index(index_name)

    # Query the index
    results = index.query(vector=query, top_k=top_k, include_values=True, include_metadata=True)

    # Filter to only contain chunks and similarity scores, return empty list if no results are found
    try:
        resultsdict = {}
        for i in results['matches']:
            resultsdict[i['metadata']['text']] = i['score']
        return resultsdict
    except Exception as e:
        print('Entered Error: ', e)
        return results