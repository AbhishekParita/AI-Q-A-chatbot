import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv('.venv')

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Q&A Bot", page_icon="🤖", layout="centered")

st.title("AI Q&A Bot")
st.markdown("Ask me anything and I'll try to help")

if 'messages' not in st.session_state:
    st.session_state.messages = []

def get_ai_response(user_question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                *st.session_state.messages,
                {"role": "user", "content": user_question}
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your question here"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ai_response(prompt)
            st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("Built with Streamlit and OpenAI")