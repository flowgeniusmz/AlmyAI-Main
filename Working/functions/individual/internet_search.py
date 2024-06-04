import streamlit as st
from tavily import TavilyClient


def internet_search(query: str):
    tavclient = TavilyClient(api_key=st.secrets.tavily.api_key)
    search = tavclient.search(query=query, search_depth="advanced", include_raw_content=True)
    return search