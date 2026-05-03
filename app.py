import streamlit as st
from groq import Groq

client = Groq(api_key="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")

st.title("My AI Chatbot 🤖")
st.write("Ask me anything!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.messages
    )
    
    ai_reply = response.choices[0].message.content
    
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    
    with st.chat_message("assistant"):
        st.write(ai_reply)