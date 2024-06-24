import streamlit as st
from config import pagesetup as ps, sessionstate as ss
from classes.user_class import User

##### 0. PAGE SETUP #####
# 0.1 Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)

# 0.2 Get page styling
ps.get_page_styling()

# 0.3 Display background
ps.display_background_image()

# 0.4 Set page title
ps.set_title_manual(varTitle="AlmyAI", varSubtitle="User Login", varDiv=True)

# 0.5 Set initial session state
if "initialized" not in st.session_state:
    ss.initialize_sessionstate()



##### 1. USER LOGIN #####
# 1.1 User login container
user_login_container = st.container(border=False)

# 1.2 Set user login container display
with user_login_container:
    if st.session_state.authenticated:
        ps.switch_to_homepage()
    else:
        ps.get_gray_header(varText="User Login")
        user_auth = User()
