import streamlit as st
from openai import OpenAI


def initialize_sessionstate():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.username = None
        st.session_state.credential = None
    if "display_messages" not in st.session_state:
        st.session_state.display_messages = [{"role": "assistant", "content": "Hi I am Almy! How can I help you today"}]
    if "client" not in st.session_state:
        st.session_state.client = OpenAI(api_key=st.secrets.openai.api_key)
        st.session_state.thread = st.session_state.client.beta.threads.create()
        st.session_state.threadid = st.session_state.thread.id
        st.session_state.assistantid = st.secrets.openai.assistant_id
        st.session_state.assistant = st.session_state.client.beta.assistants.retrieve(assistant_id=st.session_state.assistantid)
        st.session_state.run1message = st.secrets.messageconfig.run1_asst
        st.session_state.run2message = st.secrets.messageconfig.run1_asst
        st.session_state.run3message = st.secrets.messageconfig.run1_asst
        st.session_state.run4message = st.secrets.messageconfig.run1_asst
    if "runs_initialized" not in st.session_state:
        st.session_state.run1_complete = False
        st.session_state.run2_complete = False
        st.session_state.run3_complete = False
        st.session_state.run4_complete = False
        st.session_state.run1id = None
        st.session_state.run2id = None
        st.session_state.run3id = None
        st.session_state.run4id = None
        st.session_state.run1status = None
        st.session_state.run2status = None
        st.session_state.run3status = None
        st.session_state.run4status = None 
        st.session_state.runs_initialized = False
    if "initialized" not in st.session_state:
        st.session_state.initialized = True