import streamlit as st
from config import pagesetup as ps
from openai import OpenAI
import time


##### 0. PAGE SETUP #####
# 0.1 Set page config
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)

# 0.2 Set page number
page = 1

# 0.3 Set navigation menu
ps.master_page_display_styled_popmenu(varPageNumber=page)


##### 1. Container SETUP #####
main_container = ps.container_styled2(varKey="main_container")
with main_container:
    chat_container = st.container(border=True, height=300)
    with chat_container:
        for message in st.session_state.display_messages:
            with st.chat_message(name=message['role']):
                st.markdown(body=message['content'])
prompt = st.chat_input(placeholder="Type your request here...")
if prompt:
    st.session_state.display_messages.append({"role": "user", "content": prompt})
    with chat_container:
        with st.chat_message(name="user"):
            st.markdown(body=prompt)
    promptmessage = st.session_state.client.beta.threads.messages.create(thread_id = st.session_state.threadid, role="user", content=prompt)

    #Run 1
    run1_msg = st.session_state.client.beta.threads.messages.create(thread_id = st.session_state.threadid, role="assistant", content=st.session_state.run1message)
    run1 = st.session_state.client.beta.threads.runs.create(thread_id = st.session_state.threadid, assistant_id = st.session_state.assistantid, tool_choice = "none")
    while run1.status != "completed":
        time.sleep(2)
        run1 = st.session_state.client.beta.threads.runs.retrieve(thread_id = st.session_state.threadid, run_id = run1.id)
        if run1.status == "completed": 
            break

    #Run 2
    run2_msg = st.session_state.client.beta.threads.messages.create(thread_id = st.session_state.threadid, role="assistant", content=st.session_state.run1message)
    run2 = st.session_state.client.beta.threads.runs.create(thread_id = st.session_state.threadid, assistant_id = st.session_state.assistantid, tool_choice = {"type": "file_search"})
    while run2.status != "completed":
        time.sleep(2)
        run2 = st.session_state.client.beta.threads.runs.retrieve(thread_id = st.session_state.threadid, run_id = run2.id)
        if run2.status == "completed": 
            break

    #Run 3
    run3_msg = st.session_state.client.beta.threads.messages.create(thread_id = st.session_state.threadid, role="assistant", content=st.session_state.run1message)
    run3 = st.session_state.client.beta.threads.runs.create(thread_id = st.session_state.threadid, assistant_id = st.session_state.assistantid, tool_choice = {"type": "code_interpreter"})
    while run3.status != "completed":
        time.sleep(2)
        run3 = st.session_state.client.beta.threads.runs.retrieve(thread_id = st.session_state.threadid, run_id = run3.id)
        if run3.status == "completed": 
            break

    #Run 4
    run4_msg = st.session_state.client.beta.threads.messages.create(thread_id = st.session_state.threadid, role="assistant", content=st.session_state.run1message)
    run4 = st.session_state.client.beta.threads.runs.create(thread_id = st.session_state.threadid, assistant_id = st.session_state.assistantid, tool_choice = "none")
    while run4.status != "completed":
        time.sleep(2)
        run4 = st.session_state.client.beta.threads.runs.retrieve(thread_id = st.session_state.threadid, run_id = run4.id)
        if run4.status == "completed": 
            message_list = st.session_state.client.beta.threads.messages.list(thread_id = st.session_state.threadid)
            for m in message_list:
                if m.role=="assistant" and m.run_id == run4.id:
                    st.session_state.display_messages.append({"role": "assistant", "content": m.content[0].text.value})
                    with chat_container:
                        with st.chat_message(name="assistant"):
                            st.markdown(body=m.content[0].text.value)

    
