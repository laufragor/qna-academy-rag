import streamlit as st
from langchain_helper import create_vector_db, get_qa_chain

st.title("Training Academy QandA 👩🏻‍🏫")
btn = st.button("Create Knowledgebase")

if btn:
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain.invoke(question)

    if response:
        st.header("Answer: ")
        st.write(response["result"])
    else:
        st.header("Answer: ")
        st.write("There is some issue with the Application!")