
# LLM-Based RAG System

## Overview

This project is designed to create a Retrieval-Augmented Generation (RAG) system using a Large Language Model (LLM). The system integrates with an API to scrape content from the internet and uses an API to serve the LLM-generated answers. 

## Process Overview

1. **User Input via Streamlit Interface**:
   - The user interacts with a Streamlit-based front-end where they can input their query.
   - The streamlit application is formatted in a chat-bot interface

2. **Query Sent to Flask Backend**:
   - The query entered by the user is sent from the Streamlit interface to a Flask backend via an API call.
   - Chat message history is also passed to the flask backend via API call

3. **Internet Search and Article Scraping**:
   - The Flask backend searches the internet for the query using a designated API. It retrieves the top relevant articles and scrapes their content, extracting only the useful text (headings and paragraphs).

4. **Content Processing**:
   - The relavent URL for the user query are scraped using SERPER API key and then fetch the data from the links which are most related ones. Now concat all the contents from various links and process it for GPT

5. **LLM Response Generation**:
   - The processed content and the user's query along with chat history are used to generate a contextual answer using the LLM. The LLM is accessed via an API, and the generated response is returned to the Flask backend.

6. **Response Sent Back to Streamlit Interface**:
   - The Flask backend sends the generated answer back to the Streamlit interface, where it is displayed to the user.

## What we expect?
## Prerequisites

- Python 3.8 or above

## Setup Instructions

### Step 1: Clone or download the Repository (if emailed)

```bash
git clone https://github.com/venkatavinayvijjapu/DeepEdge.git
cd project_name
```

Or download it

### Step 2: Set Up a Virtual Environment

You can use `venv` or `conda` to create an isolated environment for this project.

#### Using `venv`

```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

#### Using `conda`

```bash
conda create --name project_env python=3.8
conda activate project_env
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the root directory and add your SERPER and OpenAI API keys in a way it can be accessed in the app.


### Step 5: Run the Flask Backend

Navigate to the `flask_app` directory and start the Flask server:

```bash
cd flask_app
python app.py
```

### Step 6: Run the Streamlit Frontend

In a new terminal, run the Streamlit app:

```bash
cd streamlit_app
streamlit run app.py
```

### Step 7: Open the Application

Open your web browser and go to `http://localhost:8501`. You can now interact with the system by entering your query.

## Project Structure

- **flask_app/**: Contains the backend Flask API and utility functions.
- **streamlit_app/**: Contains the Streamlit front-end code.
- **.env**: Stores API keys (make sure this file is not included in version control).
- **requirements.txt**: Lists the project dependencies.

## Video Prototype:
https://www.veed.io/view/14a2b325-2177-463b-bf16-88dbeb3d33cb?panel=share
