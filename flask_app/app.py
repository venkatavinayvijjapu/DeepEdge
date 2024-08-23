
from flask import Flask, request,jsonify
import os
from utils import *

# Load environment variables from .env file

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    """
    Handles the POST request to '/query'. Extracts the query from the request,
    processes it through the search, concatenate, and generate functions,
    and returns the generated answer.
    """
    data = request.json
    query = data.get('query')
    messages=data.get('messages')
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    # get the data/query from streamlit app
    print("Received query: ", query)
    
    
    # Step 1: Search and scrape articles based on the query
    print("Step 1: searching articles")
    articles=search_articles(query=query)
    if not articles:
        return jsonify({'answer': 'No articles found.'})

    # Step 2: Concatenate content from the scraped articles
    print("Step 2: concatenating content")
    full_text = ""
    for article in articles:
        url = article['url']
        content = fetch_article_content(url)
        processed_content = concatenate_content(content)
        full_text += processed_content + "\n\n"

    # Step 3: Generate an answer using the LLM
    print("Step 3: generating answer")
    answer = generate_answer(full_text, query,messages)

    # return the jsonified text back to streamlit
    return jsonify({'answer':answer})

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
