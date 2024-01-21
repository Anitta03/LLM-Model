#Sample Chat Boat
from langchain_openai import OpenAI

from dotenv import load_dotenv

load_dotenv() 

import streamlit as st
import os


#Function to load OpenAI model and get respones

def openai_response(question):
    model=OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0.6)
    response=model(question)
    return response

#streamlit app

st.set_page_config(page_title="Chat boat Demo")

st.header("Langchain Openai Application")

input=st.text_input("Input: ",key="input")
response=openai_response(input)

submit=st.button("Generate")

#If ask button is clicked

if submit:
    st.subheader("Respone is")
    st.write(response)
