import streamlit as st
from config import pagesetup as ps

##### 0. PAGE SETUP #####
# 0.1 Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)

# 0.2 Set page number
page = 0

# 0.3 Set navigation menu
ps.master_page_display_styled_popmenu(varPageNumber=page)


##### 1. a #####