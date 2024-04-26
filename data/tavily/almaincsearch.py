from tavily import TavilyClient
import requests
import streamlit as st

client = TavilyClient(api_key=st.secrets.tavily.api_key)
search = client.search(query="Alma Lasers Devices and Products", search_depth="advanced", include_raw_content = True, max_results = 20)
print(search)