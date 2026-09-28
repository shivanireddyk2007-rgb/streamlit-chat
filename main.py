import streamlit as st
from ollama import chat

st.title("My AI Bot: Synora")
name="Shivani"
st.write("Welcome, ",name)
question=st.text_input("Ask a question")
if st.button("Ask"):
    st.write("You asked:",question)
    response=chat(model="gemma3:1b",messages=[
        {
            "role":"system",
            "content":"You are a friendly tutor.You explain concepts in a very simple way.Explain in 50 words max."
        },
        {
            "role":"user",
            "content":question
        }
    ])
    answer=response.message.content

    st.write(answer)
 