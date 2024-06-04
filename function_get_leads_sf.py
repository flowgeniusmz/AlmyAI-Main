import streamlit as st
from simple_salesforce import Salesforce
from openai import OpenAI
import time
import json
import pandas as pd
from tavily import TavilyClient
from tempfile import NamedTemporaryFile
import pandas as pd


def create_temp_file():
    with NamedTemporaryFile(delete=False, suffix=".csv") as tfile:
        file_path = tfile.name
        return file_path
    
def create_csv_file(data):
    df = pd.DataFrame(data)
    file_path = create_temp_file()
    df.to_csv(file_path)
    return file_path

def create_openai_file(file_path):
    client = OpenAI(api_key=st.secrets.openai.api_key)
    datafile = open(file_path, "rb")
    file = client.files.create(file=datafile, purpose="assistants")
    file_id = file.id
    return file_id


def get_query_lead(zipcode: str = None):
    if zipcode is not None:
        lead_query = st.secrets.queryconfig.lead_query_zip.format(postalcode=zipcode)
    else:
        lead_query = st.secrets.queryconfig.lead_query_no_zip

    return lead_query

def get_leads_salesforce(zipcode: str=None):
    dataset = []
    sf = Salesforce(username=st.secrets.salesforce.username, password=st.secrets.salesforce.password, security_token=st.secrets.salesforce.security_token)
    query = get_query_lead(zipcode=zipcode)
    data = sf.query(query=query)
    records = data['records']
    for record in records:
        new_row = {
            'Id': record['Id'], 
            'FirstName': record['FirstName'],
            'LastName': record['LastName'],
            'Name': record['Name'],
            'Phone': record['Phone'],
            'Email': record['Email'],
            'Company': record['Company'],
            'Address': record['Address'],
            'OwnerId': record['OwnerId'],
            'Owner.Name': record['Owner']['Name'],
            'CreatedDate': record['CreatedDate']
        }
        dataset.append(new_row)
        filepath = create_csv_file(data=dataset)
        fileid = create_openai_file(file_path=filepath)
        
    return fileid


def get_leads_internet(postalcode: str):
    query = f"Contact information for medical providers, healthcare providers, doctors, clinics, and medspas that are privately owned in zip code {postalcode}"
    dataset = []
    client = TavilyClient(api_key=st.secrets.tavily.api_key)
    search = client.search(query=query, search_depth="advanced", include_raw_content=True, max_results=20, include_answer=True)
    results = search['results']
    for result in results:
        new_row = {
            'title': result['title'],
            'url': result['url'],
            'content': result['content'], 
            'raw_content': result['raw_content'],
            'score': result['score']
        }
        dataset.append(new_row)
        filepath = create_csv_file(data=dataset)
        fileid = create_openai_file(file_path=filepath)
        
    return fileid


def leads_zipcode(zipcode: str):
    a = get_leads_internet(postalcode=zipcode)
    b = get_leads_salesforce(zipcode=zipcode)
    print(a)
    print(b)


leads_zipcode(zipcode = "27006")