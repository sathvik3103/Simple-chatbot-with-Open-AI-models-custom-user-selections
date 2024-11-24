import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()

#For Langsmith Tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ["LANGCHAIN_PROJECT"]="Simple chatbot with custom selections using OpenAI"

#Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to user queries appropriately."),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    llm = ChatOpenAI(
        model=llm,
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=api_key
    )
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({"question":question})
    return answer

#App Title
st.title("Open AI Q&A Chatbot with custom selections")

#Settings 
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpeNAI API Key:",type="password")

#Dropdown
llm=st.sidebar.selectbox("Select an OpenAI Model of your choice",['gpt-4o','gpt-4-turbo','gpt-4o-mini'])

#Slider
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.5)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=500,value=250)

#Main Interface

st.write("Ask your query!")
user_input=st.text_input("You:")

if user_input and api_key:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
elif not api_key:
    st.write("Please enter your OpenAI API key in the sidebar.")
else:
    st.write("Please enter a question.")