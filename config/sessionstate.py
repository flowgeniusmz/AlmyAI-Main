import streamlit as st


def initialize_sessionstate():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.username = None
        st.session_state.credential = None