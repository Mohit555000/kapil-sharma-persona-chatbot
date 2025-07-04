import streamlit as st
from openai import OpenAI
from prompts.kapil_prompt import kapil_role_prompt
st.title("Kapil Ki Consultancy")
# Set OpenAI API key from Streamlit secrets
client=OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"]="gpt-4.1-mini"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt= st.chat_input("Hey,How can i help you today")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream=client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role":"system","content":kapil_role_prompt},
                *[
                    {"role":m["role"],"content":m["content"]}
                    for m in st.session_state.messages
                ]
               
                
            ],
            stream=True
        )
        response=st.write_stream(stream)
    st.session_state.messages.append({"role":"assistant","content":response})

