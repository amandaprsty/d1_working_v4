import streamlit as st 
from openai import OpenAI
from dotenv import load_dotenv
import os
import json 

st.write("Welcome")
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

load_dotenv()
client = OpenAI(
api_key=os.environ.get("OPENAI_API_KEY"))

if st.button("Call API"): 
        response_json = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                {
                      "role": "system", 
                      "content": "You are an AI."
                }, 
                {
                      "role": "user", 
                      "content": "Say hello. Sounds like barbie"
                }
                ]
        )

response = response_json.choices[0].message.content

st.write(response)