import streamlit as st
from langflow_module import generate_response  # Import your Langflow chatbot logic

st.title('ChatterFox - AI-Powered Customer Support Chatbot')

# Initialize session state to store the knowledge base URL
if 'knowledge_base_url' not in st.session_state:
    st.session_state['knowledge_base_url'] = ""

# Input for the knowledge base URL
knowledge_base_url = st.text_input("Enter the URL of your help page:", "https://support.spotify.com/us/category/account-help/")
if st.button("Save URL"):
    st.session_state['knowledge_base_url'] = knowledge_base_url
    st.success("Knowledge base URL saved!")

# Input for the user's question
user_input = st.text_input("Ask your question:")
if user_input:
    response = generate_response(user_input)
    st.write(response)