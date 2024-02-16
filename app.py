import streamlit as st
 
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
 
 
st.set_page_config(page_title="Building a Q&A Chatbot Using OpenAI Models")
st.header("Ask the question")
 
from dotenv import load_dotenv
load_dotenv()
import os
 
chat=ChatOpenAI(temperature=0.5)
 
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages']=[
        SystemMessage(content="Yor are a comedian AI assitant")
    ]
 
 
def get_chatmodel_response(question):
 
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer=chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content
 
input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(input)
 
submit=st.button("Response")
 
 
 
if submit:
    st.subheader("The Response is")
    st.write(response)