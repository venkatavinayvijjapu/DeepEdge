
import streamlit as st
import requests

st.title("LLM-based RAG Search")
if "messages" not in st.session_state:
   st.session_state.messages = []
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
     st.markdown (message["content"])
# Input for user query
# query = st.text_input("Enter your query:")
if query:= st.chat_input("Enter your Query...."):
    print(query)
    st.session_state.messages.append({"role": "user", "content": query})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)
    with st.spinner("Generating response..."):
        with st.chat_message("assistant"):
            flask_api_url = "http://localhost:5001/query"
            print(st.session_state.messages)
            messages = st.session_state.messages
            messages_str = ""
            for message in messages:
                if message["role"] == "user":
                    messages_str += f"User: {message['content']}///"
                elif message["role"] == "assistant":
                    messages_str += f"Assistant: {message['content']}///"
            print(messages_str)
            print("Accessing Flask API at", flask_api_url, "with query:", query)
    # Make a POST request to the Flask API
    
            response = requests.post(flask_api_url, json={"query": query,"messages":messages_str}) # call the flask app and get response
            if response.status_code == 200:
        # Display the generated answer
                answer = response.json().get('answer', "No answer received.")
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            else:
                st.error(f"Error: {response.status_code}")



