import streamlit as st
from config import pagesetup as ps
from supabase import create_client, Client
import re
import time

class User():
    def __init__(self):
        self.username = None
        self.credential = None
        self.valid_username = False
        self.authenticated = False
        self.display_user_auth_container()

    def display_user_auth_container(self):
        user_auth_container = ps.container_styled2(varKey="userauth")
        with user_auth_container:
            user_auth_cols = st.columns([1,20,1])
            with user_auth_cols[1]:
                self.username = st.text_input(label="Username", key="username")
                self.credential = st.text_input(label="Password", key="credential", type="password")
                login = st.button(label="Login", key="login", type="primary")
                if login:
                    if self.username is not None and self.credential is not None:
                        self.valid_username = self.valid_username_check()
                        if self.valid_username:
                            self.user_auth_callback()
                        else:
                            st.error(body="Please enter a valid username (email).")
                    else:
                        if self.username is None:
                            st.error(body="Please enter a valid username (email).")
                        elif self.credential is None:
                            st.error(body="Please enter a password.")
    
    def valid_username_check(self):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,3}$'       # Regular expression for validating an Email
        if re.match(pattern, self.username):
            return True
        else:
            return False

    def user_auth_callback(self):
        Client = create_client(supabase_key=st.secrets.supabase.api_key, supabase_url=st.secrets.supabase.url)
        users_table = st.secrets.supabase.table_users
        username_col = st.secrets.supabase.column_username
        credential_col = st.secrets.supabase.column_password
        select_string = f"{username_col}, {credential_col}" 
        data, _ = (Client.table(table_name=users_table).select(select_string).eq(column=username_col, value=self.username).eq(column=credential_col, value=self.credential).execute())
        lengthdata = len(data[-1])
        if lengthdata > 0:
            self.authenticated = True
            st.session_state.username = self.username
            st.session_state.credential = self.credential
            st.session_state.authenticated = True
            ps.switch_to_homepage()
        else:
            st.error(body="**ERROR**: Unable to authenticate. Please check username and password and try again.")