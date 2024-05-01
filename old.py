import streamlit as st
from config import pagesetup as ps, sessionstate as ss
import time

# Initialize session state as required
ss.initialize_sessionstate()

##### 0. PAGE SETUP #####
st.set_page_config(page_title=st.secrets.appconfig.app_name, page_icon=st.secrets.appconfig.app_icon, layout=st.secrets.appconfig.app_layout, initial_sidebar_state=st.secrets.appconfig.app_initial_sidebar)
ps.master_page_display_styled_popmenu(varPageNumber=1)

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
        

        runstatus = st.status(label="Initiating AlmyAI...", expanded=False, state="running")  # Proper use of st.status

def run_step(step_number):
    if step_number == 1 and not st.session_state.run1_complete:
        run1()
    elif step_number == 2 and not st.session_state.run2_complete:
        run2()
    elif step_number == 3 and not st.session_state.run3_complete:
        run3()
    elif step_number == 4 and not st.session_state.run4_complete:
        run4()

def run1():
    st.toast("Step 1 starting...")
    runstatus.update(label="AlmyAI is running Step 1: Reviewing user request", expanded=True, state="running")
    st.session_state.run
    time.sleep(2)  # Simulating delay
    st.session_state.run1_complete = True
    runstatus.update(label="Step 1 Completed", expanded=True, state="success")
    run_step(2)

def run2():
    st.toast("Step 2 starting...")
    runstatus.update(label="AlmyAI is running Step 2: Searching relevant knowledge via file search", expanded=True, state="running")
    time.sleep(2)
    st.session_state.run2_complete = True
    runstatus.update(label="Step 2 Completed", expanded=True, state="running")
    run_step(3)

def run3():
    st.toast("Step 3 starting...")
    runstatus.update(label="AlmyAI is running Step 3: Applying knowledge and performing tasks via code interpreter", expanded=True, state="running")
    time.sleep(2)
    st.session_state.run3_complete = True
    runstatus.update(label="Step 3 Completed", expanded=True, state="running")
    run_step(4)

def run4():
    st.toast("Step 4 starting...")
    runstatus.update(label="AlmyAI is running Step 4: Finalizing response to the user", expanded=True, state="running")
    time.sleep(2)
    st.session_state.run4_complete = True
    runstatus.update(label="AlmyAI has completed!", expanded=True, state="complete")

# Trigger the first step or appropriate step based on completion flags
if prompt:
    run_step(1 if not st.session_state.run1_complete else 
             2 if not st.session_state.run2_complete else 
             3 if not st.session_state.run3_complete else 
             4 if not st.session_state.run4_complete else 1)
