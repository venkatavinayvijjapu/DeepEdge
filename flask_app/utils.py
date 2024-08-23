import os
import requests
import logging
from bs4 import BeautifulSoup
logging.basicConfig(level=logging.INFO)
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()



# Load API keys from environment variables
SERPER_API_KEY =os.getenv("SERPER_API_KEY")
OPENAI_API_KEY =os.getenv("OPENAI_API_KEY")


def search_articles(query):
    """
    Searches for articles related to the query using Serper API.
    Returns a list of dictionaries containing article URLs, headings, and text.
    """
    headers = {
        'X-API-KEY': SERPER_API_KEY,
        'Content-Type': 'application/json'
    }
    url = 'https://google.serper.dev/search'
    payload = {
        'q': query,
        'gl': 'us',
        'hl': 'en'
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:
        logging.error(f"Error with Serper API: {response.status_code} - {response.text}")
        return []

    data = response.json()
    articles = []

    if 'organic' in data:
        for result in data['organic']:
            article_url = result.get('link')
            article_title = result.get('title')
            if article_url:
                articles.append({
                    'url': article_url,
                    'title': article_title
                })
            if len(articles)==1:
                break
    else:
        logging.warning("No 'organic' key found in response data.")

    return articles


def fetch_article_content(url):
    """
    Fetches the article content, extracting headings and text.
    """

    content = ""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': '*/*'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            headings = soup.find_all(['h1', 'h2', 'h3'])
            paragraphs = soup.find_all('p')

            content += " ".join([heading.get_text() for heading in headings])
            content += " ".join([paragraph.get_text() for paragraph in paragraphs])
        else:
            logging.error(f"Error fetching content from {url}: {response.status_code}")
    except Exception as e:
        logging.error(f"Error fetching content from {url}: {e}")
    return content.strip()

    # implementation of fetching headings and content from the articles



def concatenate_content(articles):
    
    """
    Concatenates the content of the provided articles into a single string.
    """
    return ' '.join(articles.split())

def create_history (messages):
    history = ChatMessageHistory()
    for message in messages:
       if message["role"] == "user":
         history.add_user_message(message["content"])
       else:
         history.add_ai_message(message["content"])
    return history

def generate_answer(content, query,messages):
    """
    Generates an answer from the concatenated content using GPT-4.
    The content and the user's query are used to generate a contextual answer.
    """
    client = OpenAI(api_key=OPENAI_API_KEY)
    # messages=create_history(messages)
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        
        messages=[
            {"role": "system", "content": "You are my Question expert where need to answer my queries based on content and chat history."},
            {
                "role": "user",
                "content": "Generate anser to the question: " + query + "\n\n" + content+"\n\n"+"based on the chat history "+messages
            }
        ]
    )
    response=completion.choices[0].message.content
    
    print(response)
    return response



