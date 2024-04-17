import os
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
            similar_chunks = get_similar_chunks(embedding)
            try:
                rag_output = connect_and_query_LLM(query, similar_chunks)
            except Exception as e:
                rag_output = f"An error occurred: {e}"
            return jsonify({'rag_output': rag_output})
        else:
            # Handle non-AJAX POST request if necessary
            pass
    # GET request or non-AJAX POST, render template normally
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True) 