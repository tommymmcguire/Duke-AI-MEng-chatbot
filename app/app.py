import os
import time
from flask import Flask, render_template, request, jsonify
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts.embed_query import embed_query
from scripts.get_similar_chunks import get_similar_chunks
from scripts.connect_to_LLM import connect_and_query_LLM

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            query = data['query']
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
            return jsonify({'rag_output': rag_output, 'response_time': response_time})
        else:
            # Handle non-AJAX POST request if necessary
            pass
    # GET request or non-AJAX POST, render template normally
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True) 