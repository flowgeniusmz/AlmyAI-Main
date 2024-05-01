import streamlit as st
from openai import OpenAI
import time


class Assistant():
    def __init__(self):
        self.initialize_client()
        self.initialize_assistant()
        self.initialize_thread()
        self.initialize_messages()

    def initialize_client(self):
        self.client = OpenAI(api_key=st.secrets.openai.api_key)
    
    def initialize_assistant(self):
        self.assistant=self.client.beta.assistants.retrieve(assistant_id=st.secrets.openai.assistant_id)
        self.assistant_id = self.assistant.id

    def initialize_thread(self):
        self.thread = self.client.beta.threads.create()
        self.thread_id = self.thread.id
    
    def initialize_messages(self):
        self.display_messages = []
        self.log_messages = []

    def create_message(self, prompt, role):
        self.message = self.client.beta.threads.messages.create(thread_id=self.thread_id, role=role, prompt=prompt)
        self.message_id = self.message.id

    def create_run(self):
        self.run = self.client.beta.threads.runs.create(thread_id=self.thread_id, assistant_id=self.assistant_id)
        self.run_id = self.run.id
        self.run_status = self.run_status
    
    def check_run(self):
        self.run = self.client.beta.threads.runs.retrieve(run_id=self.run_id, thread_id=self.thread_id)
        self.run_status = self.run.status
        while self.run_status != "completed":
            time.sleep(2)
            self.run = self.client.beta.threads.runs.retrieve(run_id=self.run_id, thread_id=self.thread_id)
            self.run_status = self.run.status
            if self.run_status =="completed":
                break
            elif self.run_status =="requires_action":
                break
            
